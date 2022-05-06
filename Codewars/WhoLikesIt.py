# Implement the function which takes an array containing the names of people that like an item.
# Note: For 4 or more names, the number in "and 2 others" simply increases.

def likes(names):
    if len(names) == 1:
        return '{} likes this'.format(names[0])
    if len(names) == 2:
        return '{} and {} like this'.format(names[0], names[1])
    if len(names) == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    if len(names) >= 4:
        return '{}, {} and {} others like this'.format(names[0], names[1], len(names[2:]))
    else:
        return 'no one likes this'
