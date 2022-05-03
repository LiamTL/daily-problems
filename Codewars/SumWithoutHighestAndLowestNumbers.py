# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

def sum_array(num_arr):
    if num_arr == None or len(num_arr) < 3:
        return 0
    return sum(num_arr) - max(num_arr) - min(num_arr)