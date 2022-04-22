def high_and_low(n):
    return max(n.split(' '),key=int)+' '+min(n.split(' '),key=int)