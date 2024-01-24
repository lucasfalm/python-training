my_list = [1, 2, 3, 4, 5]

for number in my_list:
  if number % 2 == 0:
    print(f"not passing from here, number '{number}'")
    pass

  if number == 3:
    print(f"finishing the loop, number '{number}'")
    break

  print(f"here! number '{number}'")

  continue

  print("never reaches here")

#
# NOTE: enumerate creates tuples with the value and the key being the index
#
for index, number in enumerate(my_list):
  print(f"now I have the index {index} and the number {number}")
