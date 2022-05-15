def divisible_by(numbers, divisor):
    divisibles = []
    for num in numbers:
        if num % divisor == 0:
            divisibles.append(num)
            
    return divisibles