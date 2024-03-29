from random import shuffle

#
# NOTE: using len()
#
some_list = [8, 4, 2, 5, 3, 1, 0]

print(f"there are {len(some_list)} objects in the list")

#
# NOTE: appending/pushing method
#
some_list.append("last")

#
# NOTE: inserting method
#
some_list.insert(0, "first")

#
# NOTE: popping
#
some_list.pop()

#
# NOTE: pop accepts an index
#
some_list.pop(0)

#
# NOTE: sorting
#
some_list.sort()

#
# NOTE: reversing
#
some_list.reverse()

#
# NOTE: counting
#
print(some_list.count(0))

#
# NOTE: check if value is in the list
#
print("a" in some_list)

some_string = "my string"

#
# NOTE: list comprehension (flat for loop - one line loop)
#
[string.upper() for string in some_string] # => ['M', 'Y', ' ', 'S', 'T', 'R', 'I', 'N', 'G']

[string.upper() for string in some_string if string == "m"] # => ['M']

#
# NOTE: shuffle a list
#
shuffle(some_list)

#
# NOTE: extend a list (append a list in a list)
#
some_list.extend([100, 500])
some_list # => [2, 8, 0, 3, 5, 1, 4, 100, 500]
