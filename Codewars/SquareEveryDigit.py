# You are asked to square every digit of a number and concatenate them.

def square_digits(num):
    string = ""
    for i in str(num):
        string += str(int(i) ** 2)
    return int(string)