# Write a function that converts any sentence into a V A P O R W A V E sentence.
#  A V A P O R W A V E sentence converts all the letters into uppercase, and adds 2 spaces between each letter
# P.S That spaces should be ignored in this case.

def vaporcode(s):
    return "  ".join(s.replace(" ", "")).upper()