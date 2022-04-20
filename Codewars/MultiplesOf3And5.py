def solution(number):
    sum = 0
    for multiple in range(number):
        if multiple % 3 == 0 or multiple % 5 == 0:
            sum += multiple
    return sum