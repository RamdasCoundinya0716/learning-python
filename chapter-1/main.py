'''
This file servers as a documentation for docstring topic. It contains examples of how to write docstrings for different Python constructs
'''
def square(n):
    '''This function takes n, a number, and returns its square.'''
    return n * n

print(square(5))  # Output: 25

print(help(square)) # Displays the docstring for the square function

'''
Naming convention for variables and functions:
_my_private_variable: This is a private variable, intended for internal use within a module or class.
my_public_variable: This is a public variable, intended for use by external code.

__private_function(): This is a private function, intended for internal use within a module or class.
my_public_function(): This is a public function, intended for use by external code.

CONSTANT_VARIABLE: This is a constant variable, typically defined at the module level and not intended to be changed.

Classess and exceptions should use the CapWords convention.
Eg: MyClass, CustomError

'''


