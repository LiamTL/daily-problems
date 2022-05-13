def how_many_dalmatians(pups):
    respond = ""
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    if pups <= 10 and pups <= 12:
        respond = dogs[0]
    
    elif pups > 12 and pups <= 50:
        respond = dogs[1]
        
    elif pups > 50 and pups < 101:
        respond = dogs[2]
    
    else:
        respond = dogs[3]
    
    return respond