# Implement a function that adds two numbers together and returns their sum in binary.
# The conversion can be done before, or after the addition.

add_binary = lambda a, b:  f'{bin(a + b)}'[2:]