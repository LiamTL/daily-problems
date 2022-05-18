def maskify(cc):
    new_string = ''
    for char in cc[0:-4]:
        new_string += '#'
        
    for num in cc[-4:]:
        new_string += num
    return new_string