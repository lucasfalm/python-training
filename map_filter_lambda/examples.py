my_list = [1, 2, 3, 4]

def is_odd(number):
  return number % 2 != 0

def is_even(number):
  return number % 2 == 0

# ------------ X ------------ X ------------ #

#
# NOTE: filter method
#

my_odd_list = list(filter(is_odd, my_list))

my_even_list = list(filter(is_even, my_list))

print(my_odd_list, my_even_list)

# ------------ X ------------ X ------------ #

#
# NOTE: map method
#

my_new_list = list(map(lambda number: number * 2, my_list)) # using lambda (anonymous function)

print(my_new_list)

# ------------ X ------------ X ------------ #

def format_number(number):
  return f"#{str(number)}"

my_other_new_list = list(map(format_number, my_list))

print(my_other_new_list)
