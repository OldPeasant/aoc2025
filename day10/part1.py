import sys

sys.path.append('../lib')
from pmg import *


def find_min_pushes(goal, buttons):
    count = 1
    while True:
        c = count
        curr = list(0 for i in range(len(goal)))
        for b in buttons

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    button_presses = 0
    for l in lines:
        parts = l.split(" ")
        goal = parts[0][1:-1]
        buttons = list( (list(int(i) for i in b[1:-1].split(","))) for b in parts[1:-1])
        joltage = list( int(i) for i in parts[-1][1:-1].split(","))
        print(goal, buttons, joltage)
        min_buttons = find_min_pushes(goal, buttons)
        button_presses += min_buttons
        #bla = list(0 for i in range(len(goal)))
        #print(bla)
    print(button_presses)
