import timeit
setup_1 = "import math"
setup_2 = "import numpy as np"

code_1 = '''
def example():
    math.sqrt(1337)
'''

code_2 = '''
def example():
    np.sqrt(1337)
'''

code_3 = '''
def example():
    1337**0.5
'''
 
# math.sqrt(1337)
print (timeit.timeit(setup = setup_1,
                     stmt = code_1,
                     number = 10000))
#output: 0.0010587689466774464

# np.sqrt(1337)
print (timeit.timeit(setup = setup_2,
                     stmt = code_2,
                     number = 10000))
#output: 0.0008163549937307835

# 1337**0.5
print (timeit.timeit(stmt = code_3,
                     number = 10000))
#output: 0.0005355479661375284