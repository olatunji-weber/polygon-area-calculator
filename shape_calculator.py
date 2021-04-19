class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    shapeString = f"Rectangle(width={self.width}, height={self.height})"
    return shapeString

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    #returns area ('width * height')
    return self.width * self.height

  def get_perimeter(self):
    #returns diagonal((width**2 + height**2) **.5)
    return (2*self.width + 2*self.height)
  
  def get_diagonal(self):
    return ((self.width**2 + self.height**2) ** 0.5)

  def get_picture(self):
    image = ""
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      image = ((("*" * self.width) + "\n")* self.height)
      return image    
  
  def get_amount_inside(self, shape):
    numberOfTimes = self.get_area() // shape.get_area()
    return numberOfTimes

class Square(Rectangle):
  def __init__(self, length):
    self.width = length
    self.height = length

  def __str__(self):
    shapeString = f"Square(side={self.width})"
    return shapeString

  def set_side(self, length):
    self.height = length
    self.width = length