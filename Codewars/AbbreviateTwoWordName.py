# Convert name to uppercase
# Split string
# Get first letters
# Return + join letters with a seperating "."

def abbrev_name(name):
    uppername = name.upper()
    words = uppername.split()
    letters = [word[0] for word in words]
    return (".".join(letters))