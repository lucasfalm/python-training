#
# NOTE: functions are objects that can be passed to other functions
#
def custom_func(option):
  def inner_func_one():
    print("inner one")

  def inner_func_two():
    print("inner two")

  if option == 1: return inner_func_one # returning the function as an object
  if option == 2: return inner_func_two # same
  else:
    print("option not found")

my_func = custom_func(option = 1)

if my_func:
  my_func()
