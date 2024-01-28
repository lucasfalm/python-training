#
# NOTE: generators are a memory efficient way to
#       "store" (or in this case, generate) a list
#

# ------------ X ------------ X ------------ #

def my_generator():
  for number in range(5):
    #
    # NOTE: every time next(my_generator()) is called, the next
    #       yielded value takes place (as if it was going through each element in the list)
    #
    yield number

def opposite_of_my_generator():
  numbers = [] # need a list to store the results (using memory)

  for number in range(5):
    numbers.append(number)

  return numbers

# ------------ X ------------ X ------------ #

print(my_generator()) # => <generator object my_generator at 0x1021b82b0>
print(list(my_generator())) # => [0, 1, 2, 3, 4]
print(next(my_generator())) # => 0
print(next(my_generator())) # => 1
print(next(my_generator())) # => 2
print(next(my_generator())) # => 3
print(next(my_generator())) # => 4

