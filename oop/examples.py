# ------------ X ------------ X ------------ #

class ParentClass():
  def __init__(self):
    print("creating the parent object")

  def say_hi(self):
    print("hi from the ParentClass")

# ------------ X ------------ X ------------ #

class MyClass(ParentClass):
  #
  # NOTE: this is equal for all instances of MyClass
  #
  class_common_attribute = "something"

  def class_method():
    print("I'm a class method")

  def __init__(self, name):
    super().__init__()

    print("creating the child object")

    self.name = name

  def say_hi(self):
    #
    # NOTE: from the self you can access the private methods
    #
    self.__some_private_method()

    #
    # NOTE: can call the parent but still use the children implementation
    #
    super().say_hi()

    print(f"hi, {self.name}! (from the MyClass)")

  #
  # NOTE: private methods are available only to the object
  #
  def __some_private_method(self):
    print("I'm a private method, don't call me directly")

  #
  # NOTE: protected methods are available to the family (parent/s)
  #
  def _some_protected_method(self):
    print("I'm a protected method, don't call me directly")

  def print_class_attribute(self):
    #
    # NOTE: can be called in two ways
    #
    #       a common approach is the first ('MyClass.') option
    #       to make it clear that this is a class attribute
    #
    print(f"my class attribute is '{MyClass.class_common_attribute}'")
    print(f"my class attribute can be called like this too '{self.class_common_attribute}'")

# ------------ X ------------ X ------------ #

my_object = MyClass(name = "lucas") # this is the '.new'

my_object.say_hi()

print(my_object.name)

print(MyClass.class_common_attribute)

MyClass.class_method()

my_object.print_class_attribute()

#
# NOTE: possible to call from outside too (don't do it)
#
#       python don't have the concept of access control, but conventions
#
#       you can add __ to the front of the method and it will be 'private'
#       python will name mangle the method name to avoid naming conflicts
#       and the method name will be the _class_name + __method_name
#
my_object._MyClass__some_private_method()

#
# NOTE: protected method names are not mangled as the privates are
#
my_object._some_protected_method()
