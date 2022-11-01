# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b keeping their order.

def array_diff(a, b):
    diff = []
    if a == [] or a == None:
        return []

    for num in range(len(a)):
        if a[num] not in b:
            diff.append(a[num])
    return diff