def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s