def spin_words(sentence):
    words = sentence.split(" ")
    result = ""
    for word in words:
        count = len(word)
        if count >= 5:
            result += word[::-1] + " "
        elif count < 5:
            result += word + " "
    return result[0:len(result) - 1]