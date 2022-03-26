# Write a function which calculates the average of the numbers in a given list.

def find_average(numbers):
    avrg = 0
    for i in range(len(numbers)):
        avrg += numbers[i]
    
    return avrg / len(numbers)