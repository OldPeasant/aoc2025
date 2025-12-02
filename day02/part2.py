import sys

sys.path.append('../lib')
from pmg import *

def is_invalid(s):
    print("----------------")
    print(s)
    ls = len(s)
    print(int(len(s)/2))
    for i in range(1, 1 + int(len(s)/2)):
        if ls % i == 0:
            first = s[:i]
            for j in [1:i]:
                sub = s[j
        print(i)
    return False
    #if len(s) % 2 == 0:
    #    lh = int(len(s)/2)
    #    if s[:lh] == s[lh:]:
    #        return True
    #return False

with open(sys.argv[1]) as f:
    lines = f.read().split(",")

    total = 0
    for l in lines:
        lo, high = (int(n) for n in l.split("-"))
        print(lo, high)
        n = lo
        while n <= high:
            s = str(n)
            if is_invalid(s):
                total += n
            n += 1
    print(total)
