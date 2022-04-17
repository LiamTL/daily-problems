def sum_mix(arr_of_strng_and_ints):
    result = 0
    for val in arr_of_strng_and_ints:
        try:
            result += val
        except TypeError:
            result += int(val)
    return result