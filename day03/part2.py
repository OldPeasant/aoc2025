import sys

sys.path.append('../lib')
from pmg import *

def calc_joltage(line, length):
    print("calc_joltage", line, length)
    numbers = list(int(i) for i in line)
    highest = max(numbers[:len(line) - length + 2])
    print("highest", highest)
    if length == 2:
        print("length is 1", highest)
        return str(highest)
    pos_first = numbers.index(highest)
    second = calc_joltage(line[pos_first+1:], length - 1)

    joltage = str(highest) + second
    print(numbers, highest, pos_first, second, joltage)
    return joltage

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    total = 0
    for l in lines:
        joltage = int(calc_joltage(l, 13))
        total += joltage
        print(joltage, total)
    print(total)
