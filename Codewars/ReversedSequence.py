# Build a function that returns an array of integers from n to 1 where n>0.

def reverse_seq(n):
    output = []
    for i in range(n):
        output.append(n)
        n -= 1
    return output