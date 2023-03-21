# This time no story, no theory.

def accum(s):
    mumble = ""
    for idx in range(0, len(s)):
        mumble += s[idx].upper()
        mumble += s[idx].lower() * idx
        if idx != len(s) - 1:
            mumble += '-'
    return mumble