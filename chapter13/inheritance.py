class Vehicle:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def get_make(self):
    return self.make

  def get_model(self):
    return self.model

  def __str__(self):
    return 'make: {}, model: {}'.format(self.make, self.model)


class Car(Vehicle):
  def __init__(self, make, model, num_doors):
    Vehicle.__init__(self, make, model)
    self.num_doors = num_doors


v = Vehicle('cat', 'zc100')
c = Car('dodge', 'caravan', '4')

print('c is v ? {}'.format(c is v))
print('instance of Car is Vehicle? {}'.format(isinstance(c, Vehicle)))
print(v)
print(c)
