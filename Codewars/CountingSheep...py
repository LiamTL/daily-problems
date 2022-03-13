# Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    count_sheps = 0
    for i in range(len(sheep)):
        if sheep[i] == True: 
            count_sheps += 1
    return count_sheps