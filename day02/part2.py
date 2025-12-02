import sys

sys.path.append('../lib')
from pmg import *

def is_invalid(s):
    ls = len(s)
    for i in range(1, 1 + int(len(s)/2)):
        if ls % i == 0:
            first = s[:i]
            all_match = True
            for j in range(1, int(ls/i)):
                item = s[j*i: (j+1) * i]
                if item != first:
                    all_match = False
                    break
            if all_match:
                return True
    return False

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
