def find_multiples(integer, limit):
    multiples = []
    for multiple in range(integer, limit + 1):
        if multiple % integer == 0:
            multiples.append(multiple)
    return multiples