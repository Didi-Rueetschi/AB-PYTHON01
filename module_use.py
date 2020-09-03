# User-defined modules

# File: module_new.py

#   def square(x):
#       erg = x * x
#       return erg

#main program: Modules.py
import module_new as mn
z = mn.square(3)
print(z)

# or

from module_new import square
z = square(3)
print(z)
