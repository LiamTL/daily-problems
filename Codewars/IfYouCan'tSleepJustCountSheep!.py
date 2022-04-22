def count_sheep(num_of_sheep):
    sheep = ""
    for sheep_num in range(1, num_of_sheep+1):
        sheep += f"{sheep_num} sheep..."
    return sheep