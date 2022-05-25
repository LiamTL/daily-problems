def descending_order(num):
    # Bust a move right here
    digitList = [int(x) for x in str(num)]
    digitList.sort()
    digitList.reverse()
    return int(''.join(str(i) for i in digitList))
    # Busted a move ere 😎😎