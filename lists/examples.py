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
