# Return the number (count) of vowels in the given string.

def get_count(sentence):
    valid_vows = "aeiouAEIOU"
    vows_found = 0
    for poss_vow in sentence:
        if poss_vow in valid_vows:
            vows_found += 1
            
    return vows_found
        
