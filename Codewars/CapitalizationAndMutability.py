# Your coworker was supposed to write a simple helper function to capitalize a string (that contains a single word) before they went on vacation.
# Unfortunately, they have now left and the code they gave you doesn't work. Fix the helper function they wrote so that it works as intended

capitalize_word = lambda word: f"{word[0].capitalize() + word[1:len(word)]}"