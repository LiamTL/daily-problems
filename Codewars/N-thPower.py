# You are given an array with positive numbers and a non-negative number N. 
# You should find the N-th power of the element in the array with the index N.
def index(array, n):
    try:
        return array[n] ** n
    except:
        return -1