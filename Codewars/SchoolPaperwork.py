# Your classmates asked you to copy some paperwork for them.
# You know that there are 'n' classmates and the paperwork has 'm' pages.

def paperwork(n, m):
    if m <= 0 or n <= 0:
        return 0
    return n * m