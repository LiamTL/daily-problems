def disemvowel(string):
    vowels = "aeiouAEIOU"
    fixxed = ""
    for vow_idx in range(len(string)):
        if string[vow_idx] not in vowels:
            fixxed += string[vow_idx]
            
    return fixxed