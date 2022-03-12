# Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    result = 0
    for num in numbers:
        result = result + num ** 2
    return result
        