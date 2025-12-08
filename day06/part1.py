import sys
from functools import reduce
import operator

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    rows = [ [] for i in range(len(lines))]

    for ix, l in enumerate(lines):
        stripped = " ".join(l.split())
        for e in stripped.split(" "):
            rows[ix].append(e)
    total = 0
    for i in range(len(rows[0])):

        numbers = list(int(r[i]) for r in rows[:-1])
        op = rows[-1][i]
        print(numbers, op)

        res = reduce(operator.add if op == "+" else operator.mul, numbers)
        print(res)
        total += res
    print(total)
