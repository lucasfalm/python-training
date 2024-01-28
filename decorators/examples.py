#
# NOTE: you can decorate functions or classes
#

# ------------ X ------------ X ------------ #

def my_decorator(original_function):
  def wrap():
    print("executed before the function")

    original_function()

    print("executed after the function\n")

    return True

  return wrap

# ------------ X ------------ X ------------ #

#
# NOTE: by using the 'at' (@), python will executed the 'my_decorator'
#       and use the 'some_function' as parameter ('original_function')
#
@my_decorator
def some_function():
  print("executing something...")

#
# NOTE: when I call 'some_function' it's actually calling the 'wrap'
#
some_function # -> <function my_decorator.<locals>.wrap at 0x1001447c0>

some_function() # =>
# executed before the function
# executing something...
# executed after the function

# ------------ X ------------ X ------------ #

#
# NOTE: it can also be used with classes
#

# ------------ X ------------ X ------------ #

def my_class_decorator(original_class):
  class Wrap(original_class):
    def __init__(self):
      print("executed before the initialization")
      super().__init__()

      print("executed after the initialization")

    def some_method(self):
      print("executed before the method")

      super().some_method()

      print("executed after the method")

  return Wrap

# ------------ X ------------ X ------------ #

@my_class_decorator
class MyClass():
  def __init__(self):
    pass

  def some_method(self):
    print("inside the object")

my_object = MyClass()
my_object.some_method() # =>
# executed before the function
# executing something...
# executed after the function
#
# executed before the initialization
# executed after the initialization
# executed before the method
# inside the object
# executed after the method