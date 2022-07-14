def xo(s):
    xs, os = 0, 0
    
    for char in s:
        if char == "x" or char == "X":
            xs += 1
        elif char == "o" or char == "O":
            os += 1
        
    return xs == os