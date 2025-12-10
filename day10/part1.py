import sys

sys.path.append('../lib')
from pmg import *

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()


    for l in lines:
        parts = l.split(" ")
        goal = parts[0][1:-1]
        buttons = list( (list(int(i) for i in b[1:-1].split(","))) for b in parts[1:-1])
        joltage = list( int(i) for i in parts[-1][1:-1].split(","))
        print(goal, buttons, joltage)
        bla = list(0 for i in range(len(goal)))
        print(bla)
