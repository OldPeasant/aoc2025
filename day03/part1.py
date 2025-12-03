import sys

sys.path.append('../lib')
from pmg import *

def calc_joltage(line):
    numbers = list(int(i) for i in line)
    highest = max(numbers[:-1])
    pos_first = numbers.index(highest)
    second = max(numbers[pos_first+1:])
    joltage = 10 * highest + second
    print(numbers, highest, pos_first, second, joltage)
    return joltage

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    total = 0
    for l in lines:
        joltage = calc_joltage(l)
        total += joltage
        print(joltage, total)
    print(total)
