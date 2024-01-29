import random

my_list = list(range(10))

#
# NOTE: sample
#
random.choice(my_list) # => 8

#
# NOTE: sample multiples (can sample the same twice)
#
random.choices(population=my_list, k = 5) # => [8, 1, 5, 4, 8]

#
# NOTE: sample multiples (cannot sample the same twice)
#
random.sample(population=my_list, k = 2) # => [5, 7]

#
# NOTE: shuffle (affect the list)
#
random.shuffle(my_list)

print(my_list) # => [6, 3, 5, 0, 1, 9, 8, 2, 4, 7]
