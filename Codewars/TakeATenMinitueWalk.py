# I know there are shorter solutions than this but I only do solutions I understand
# (If I don't get the solution look at solution but I don't copy and paste.)
# (There is no worth of knowledge in it!)
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
# Check if the walk is less than 10 minitues
def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    x_pos = 0
    y_pos = 0
    
    for direction in walk:
        if direction == 'n':
            y_pos += 1
        elif direction == 's':
            y_pos -= 1
        elif direction == 'e':
            x_pos += 1
        else:
            x_pos -= 1

    if x_pos == 0 and y_pos == 0:
        return True
    return False
