def abbrev_name(name):
    # Convert name to uppercase
    uppername = name.upper()
    # Split string
    words = uppername.split()
    # Get first letters
    letters = [word[0] for word in words]
    # Return + join letters with a seperating "."
    return (".".join(letters))