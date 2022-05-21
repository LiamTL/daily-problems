def make_chocolates(small, big, goal):
    for check_big in range(min(big, goal//5), -1, -1):
        for check_small in range(small+1):
            if 5 * check_big + 2 * check_small == goal:
                return check_small
    return -1