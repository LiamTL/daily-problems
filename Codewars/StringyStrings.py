def stringy(size):
    res_str = ""
    for num in range(1, size + 1):
        if num % 2 == 0:
            res_str += "0"
        elif num % 2 != 0:    
            res_str += "1"
    return res_str
        
# Create a string to store 1's and 0's
# Make a for loop to iterate from one to size + 1
#   Check the variable if it's even or odd
#   If it is even append 0 to the result else append 1
# Return the result