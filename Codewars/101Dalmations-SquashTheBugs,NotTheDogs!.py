def how_many_dalmations(dogs):
    response = ""
    pups = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    if dogs <= 10 and dogs <= 12:
        response = pups[0]
    elif dogs > 12 and dogs <= 50:
        response = pups[1]
    elif dogs > 50 and dogs < 101:
        response = pups[2]
    else:
        response = pups[3]
    return response