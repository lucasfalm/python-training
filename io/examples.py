file_path = "io/file.txt"

my_file = open(file_path)

#
# NOTE: this prints the content
#
print(my_file.read())

#
# NOTE: this prints nothing
#
print(my_file.read())

#
# NOTE: need to reset the cursor after reading
#
my_file.seek(0)

#
# NOTE: this prints the content again
#
print(my_file.read())

my_file.seek(0)

print(my_file.readlines())

my_file.seek(0)

for line in my_file.readlines():
  print(f"this is a line: {line}")

#
# NOTE: remember to close the file
#
my_file.close()

#
# NOTE: this will auto close the file after using it
#
with open(file_path) as opened_my_file:
  print(opened_my_file.read())

#
# NOTE: writing to the file
#
with open(file_path, "w+") as opened_my_file:
  opened_my_file.write("that's a new line\n")
  print(opened_my_file.read())
