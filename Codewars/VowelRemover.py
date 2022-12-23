def shortcut( s ):
    vowels = "aeiou"
    removed = ""
    for char in range(len(s)):
        if s[char] not in vowels:
            removed += s[char]
    return removed