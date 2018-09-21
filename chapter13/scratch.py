# from test import testEqual

class Point:

  def __init__(self, init_x, init_y):
      """ Create a new point at the given coordinates. """
      self.x = init_x
      self.y = init_y

  def get_x(self):
      return self.x

  def get_y(self):
      return self.y

  def distance_from_origin(self):
      return ((self.x ** 2) + (self.y ** 2)) ** 0.5

  def __repr__(self):
      return "x=" + str(self.x) + ", y=" + str(self.y)


class Rectangle:
  """Rectangle class using Point, width and height"""

  def __init__(self, init_p, init_w, init_h):

      self.location = init_p
      self.width = init_w
      self.height = init_h

  def __repr__(self):
      return "I'm a rectangle with width {} and height {}".format(self.width, self.height)

  def transpose(self):
      temp = self.width
      self.width = self.height
      self.height = temp

  def contains(self, point):
    or_x = self.location.get_x()
    or_y = self.location.get_y()

    x_limit = or_x + self.width
    y_limit = or_y + self.height

    return or_x <= point.x < x_limit and or_y <= point.y < y_limit
    # return int(point.x) in range(or_x, x_limit) and int(point.y) in range(or_y, y_limit)

r = Rectangle(Point(0, 0), 10, 4.1)
print(r.contains(Point(0, 0))) # True)
print(r.contains(Point(3, 3))) # True)
print(r.contains(Point(3, 7))) #, False)
print(r.contains(Point(3, 5))) #, False)
print(r.contains(Point(3, 4.99999))) #, True)
print(r.contains(Point(-3, -3))) #, False)
