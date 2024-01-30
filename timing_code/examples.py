import timeit

#
# NOTE: triple quotes create multi line string
#
statement_one = '''
list(func_one(1000))
'''

setup_one = '''
def func_one(qtd):
  return(range(qtd))
'''

statement_two = '''
list(func_two(1000))
'''

setup_two = '''
def func_two(qtd):
  for number in range(qtd): yield number
'''

timeit.timeit(statement_one, setup_one, number=100000) # => 0.683117750000747

timeit.timeit(statement_two, setup_two, number=100000) # => 2.3740287500004342
