def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump == 50 and fuel_left >= 2:
        return True
    return False