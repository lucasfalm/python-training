dictionary = { "first_key": "hey", "second_key": { "third_key": "yo" } }

#
# NOTE: accessing keys
#
print(f"{dictionary['first_key']} {dictionary.get('second_key').get('third_key') }")

#
# NOTE: using values
#
print(dictionary.values())

#
# NOTE: using each object
#
print(dictionary.items())

#
# NOTE: adding values
#
dictionary.update({ "fourth_key": "oh yeah" })

dictionary["fifth_key"] = "it also works"

print(dictionary.values())

for key, item in dictionary.items():
  print(f"I'm '{item}' from key '{key}'")

#
# NOTE: deleting keys
#
print(dictionary.pop("fifth_key"))