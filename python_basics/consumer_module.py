import first_module

print(first_module.absolute(-9))

from first_module import square

print(square(5))

from first_module import *

print(sum_([9, 8, 5, 3, 5, 6]))
