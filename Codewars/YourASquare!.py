# Given an integral number, determine if it's a square number
import math

def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;