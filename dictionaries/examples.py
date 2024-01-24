dictionary = { "first_key": "hey", "second_key": { "third_key": "yo" } }

#
# NOTE: accessing keys
#
f"{dictionary['first_key']} {dictionary.get('second_key').get('third_key') }"

#
# NOTE: using values
#
dictionary.values()

#
# NOTE: using each object
#
dictionary.items()

#
# NOTE: adding values
#
dictionary.update({ "fourth_key": "oh yeah" })

dictionary["fifth_key"] = "it also works"

#
# NOTE: doing a, b is known as tuple packing
#
for key, item in dictionary.items():
  print(f"I'm '{item}' from key '{key}'")

#
# NOTE: deleting keys
#
print(dictionary.pop("fifth_key"))
