#
# NOTE: using str#format
#
some_string = "hey you, {}! {}".format("Lucas", "welcome to Python!")

#
# NOTE: possible to pass index positions
#
other_string = "that's {1}, isn't {0}?".format("it", "cool")

#
# NOTE: and aliases (and also optionally using 'f' instead of '.format' - new version)
#
i, c = "it", "cooler"
another_string = f"I think this is even {c}, isn't {i}?"

#
# NOTE: formatting floats/precisions { value:width.precision f }
#
precision_float_string = "the result is {n:1.3f}".format(n=3.1209302)

print(some_string)
print(other_string)
print(another_string)
print(precision_float_string)

#
# NOTE: reversing a string
#
my_name = "Lucas"
my_name[::-1] # => sacuL