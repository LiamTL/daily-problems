# Write a function find_needle() that takes an array full of junk but containing one "needle"

def find_needle(haystack):
    idx_count = 0
    for possib_needle in haystack:
        if possib_needle == "needle":
            return f"found the needle at position {idx_count}"
        idx_count += 1