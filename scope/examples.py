#
# NOTE: global variable
#
x = 0

def some_function():
  #
  # NOTE: local variable
  #
  x = 1

  print(x) # => 1

def some_other_function():
  global x

  #
  # NOTE: local assignment changing the global value of x
  #
  x = 2

  print(x) # => 2

print(x) # => 2

def better_way_function(x):
  x = 3 # local change only

  return x

x = better_way_function(x) # changing the global value of x