# Return the number (count) of vowels in the given string.

def get_count(sentence):
    vow_count = 0
    for vow in sentence:
        if vow == "a" or vow == "e" or vow == "i" or vow == "o" or vow == "u":
            vow_count += 1
    return vow_count