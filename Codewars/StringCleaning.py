# Your program will take in a string and clean out all numeric characters, and return a string with spacing and special characters ~#$%^&!@*():;"'.,? all intact.
# Your harried co-workers are looking to you for a solution to take this garbled text and remove all of the numbers. 

def string_clean(s):
    cleaned_str = ""
    for item in s:
        if item.isdigit() == False:
            cleaned_str += item
    return cleaned_str
    