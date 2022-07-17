# Your task is to convert strings to how they would be written by Jaden Smith.

def to_jaden_case(string):
    tweet_lst = string.split()
    for idx in range(len(tweet_lst)):
        tweet_lst[idx] = tweet_lst[idx].capitalize()
    
    return " ".join(tweet_lst)