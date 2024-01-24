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

