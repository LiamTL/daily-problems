# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def digitize(n):
    num_array = [] # make an empty array
    for number in str(n): # make n into string to iterate through 
        num_array.insert(0, int(number)) # insert the number into 1st position (reversing it)
    return num_array # return the array