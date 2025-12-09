import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    red = []
    for l in lines:
        col, row = (int(n) for n in l.split(","))
        red.append( (col, row) )

    max_area = -1
    for r1 in red:
        for r2 in red:
            a = abs(r2[1] - r1[1] + 1) * abs(r2[0] - r1[0] + 1)
            print(r1, r2, a)
            if a > max_area:
                max_area = a
    print(max_area)
