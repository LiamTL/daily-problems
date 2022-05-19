# Odd name for a kata isn't it??? (Function also)

def is_kiss(words):
    words = words.split()
    for word in words:
        if len(word) > len(words):
            return "Keep It Simple Stupid"
    return "Good work Joe!"