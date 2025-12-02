import sys

sys.path.append('../lib')
from pmg import *

with open(sys.argv[1]) as f:
    lines = f.read().split(",")

    total = 0
    for l in lines:
        lo, high = (int(n) for n in l.split("-"))
        print(lo, high)
        n = lo
        while n <= high:
            s = str(n)
            print(s)
            if len(s) % 2 == 0:
                lh = int(len(s)/2)
                if s[:lh] == s[lh:]:
                    print("invalid", s)
                    total += n
            n += 1
    print(total)
