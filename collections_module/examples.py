# ------------ X ------------ X ------------ #

from collections import Counter

my_list         = [1, 2, 3, 4, 5, 6, 6, 2, 1, 1, 1, 1, 1, 1]
my_list_counter = Counter(my_list)

print(my_list_counter) # => Counter({1: 7, 2: 2, 6: 2, 3: 1, 4: 1, 5: 1})

# ------------ X ------------ X ------------ #

from collections import defaultdict

#
# NOTE: in case the requested key does not exist it will return '0' (default value)
#
my_dic = defaultdict(lambda: 0)

print(my_dic["key_two"]) # => 0

# ------------ X ------------ X ------------ #

from collections import namedtuple

#
# NOTE: a named tuple helps to identify/fetch the items by name instead of index
#

Number = namedtuple("Number", ["value", "type"])

number_one = Number(value = 1, type = "odd")
number_two = Number(value = 2, type = "even")

number_one.value
number_one.type