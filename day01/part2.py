import sys

sys.path.append('../lib')
from pmg import *

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    dir = {"L": -1, "R": 1}
    dial = 50
    count_zero = 0
    for l in lines:
        print("--------------------------")
        val = dir[l[0]] * int(l[1:])
        dial += val
        pre = dial
        print(dial, count_zero)
        while dial < 0:
            count_zero += 1
            dial += 100
            print(" ->")
        print(dial, count_zero)
        while dial > 99:
            count_zero += 1
            dial -= 100
            print(" <-")
        print(dial, count_zero)
        print(val, pre, dial, dial >= 0, dial <=99, count_zero)
        if dial == 0:
            count_zero += 1
    print(count_zero)
