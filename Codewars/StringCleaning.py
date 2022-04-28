def string_clean(s):
    cleaned_str = ""
    for item in s:
        if item.isdigit() == False:
            cleaned_str += item
    return cleaned_str
    