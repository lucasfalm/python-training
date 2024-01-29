# ------------ X ------------ X ------------ #

from collections import Counter

my_list         = [1, 2, 3, 4, 5, 6, 6, 2, 1, 1, 1, 1, 1, 1]
my_list_counter = Counter(my_list)

print(my_list_counter) # => Counter({1: 7, 2: 2, 6: 2, 3: 1, 4: 1, 5: 1})

# ------------ X ------------ X ------------ #
