# make a new string to store the result
# iterate through input string
# if the current element is not a space add it to the new string
# return new string

def no_space(x):
    result = ""
    for idx in x:
        if idx != " ":
            result = result + idx
    return result