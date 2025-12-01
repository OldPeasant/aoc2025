import sys

sys.path.append('../lib')
from pmg import *

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    dir = {"L": -1, "R": 1}
    dial = 50
    count_zero = 0
    for l in lines:
        val = dir[l[0]] * int(l[1:])
        print(val)
        dial += val
        while dial < 0:
            dial += 100
        while dial > 99:
            dial -= 100
        print("    ", dial, dial >= 0, dial <=99)
        if dial == 0:
            count_zero += 1
    print(count_zero)
