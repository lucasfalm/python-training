#
# NOTE: a set is a list with unique items
#

#
# NOTE: creating a set
#
some_set = set()

#
# NOTE: adding to the set
#
some_set.add("1")
some_set.add("2")
some_set.add("2")

other_set = set(["1", "3"])

some_set.difference(other_set)

some_set.union(other_set)

some_set.symmetric_difference(other_set)

#
# NOTE: cast list to set (make unique items)
#
my_list = ["1", "2", "2"]
set(my_list)
