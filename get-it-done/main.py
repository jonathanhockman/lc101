from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://get-it-done:beproductive@localhost:3306/get_it_done'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
app.secret_key = 'y337kGcys&zP3B'

class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    completed = db.Column(db.Boolean)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, owner):
        self.name = name
        self.completed = False
        self.owner = owner


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    tasks = db.relationship('Task', backref='owner')

    def __init__(self, email, password):
        self.email = email
        self.password = password

@app.before_request
def require_login():
    allowed_routes = ['get_login', 'post_login', 'register']
    if request.endpoint not in allowed_routes and 'email' not in session:
        return redirect('/login')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def post_login():
    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        session['email'] = email
        flash("Logged in")
        return redirect('/')

    flash('User password incorrect, or user does not exist', 'error')
    return render_template('login.html')


def email_valid(email):
    if not ('@' in email):
        return False

    if len(email) <= 4:
        return False

    if not ('.' in email):
        return False

    if ' ' in email:
        return False

    return True


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']

        existing_user = User.query.filter_by(email=email).first()
        if not existing_user:
            email_good = email_valid(email)
            pass_good = password == verify and len(password) > 4

            if email_good and pass_good:
                new_user = User(email, password)
                db.session.add(new_user)
                db.session.commit()
                session['email'] = email
                return redirect('/')

            return "<h1>Invalid information</h1>"
        else:
            # TODO - user better response messaging
            return "<h1>Duplicate user</h1>"

    return render_template('register.html')

@app.route('/logout')
def logout():
    del session['email']
    return redirect('/')


@app.route('/', methods=['POST', 'GET', 'PUT'])
def index():
    owner = User.query.filter_by(email=session['email']).first()

    if request.method == 'POST':
        task_name = request.form['task']
        new_task = Task(task_name, owner)
        db.session.add(new_task)
        db.session.commit()

    elif request.method == 'PUT':
        task_id = int(request.form['task-id'])
        task = Task.query.filter_by(id=task_id,owner=owner).first()
        task.completed = True
        db.session.add(task)
        db.session.commit()

    tasks = Task.query.filter_by(completed=False,owner=owner).all()
    completed_tasks = Task.query.filter_by(completed=True,owner=owner).all()
    return render_template('todos.html',title="Get It Done!",
        tasks=tasks, completed_tasks=completed_tasks)


if __name__ == '__main__':
    app.run()