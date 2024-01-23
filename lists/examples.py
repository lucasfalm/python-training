#
# NOTE: using len()
#
some_list = [8, 4, 2, 5, 3, 1, 0]

print(f"there are {len(some_list)} objects in the list")

#
# NOTE: appending/pushing method
#
some_list.append("last")
print(some_list)

#
# NOTE: inserting method
#
some_list.insert(0, "first")
print(some_list)

#
# NOTE: popping
#
some_list.pop()
print(some_list)

#
# NOTE: pop accepts an index
#
some_list.pop(0)
print(some_list)

#
# NOTE: sorting
#
some_list.sort()
print(some_list)

some_list.reverse()
print(some_list)
