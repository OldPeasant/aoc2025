import sys

def multi_list(*args, value=None):
    if len(args) > 1:
        return [ multi_list(*list(args)[1:], value=value) for x in range(args[0])]
    else:
        return [value for x in range(args[0])]

class Grid:
    def __init__(self, width, height, value=None):
        self.data = multi_list(width, height, value=value)

    def set(self, x, y, v):
        self.data[x][y] = v

    def get(self, x, y):
        return self.data[x][y]
def connect(grid, r1, r2):
    print("Connect", r1, r2)
    x1 = min(r1[0], r2[0])
    x2 = max(r1[0], r2[0])
    y1 = min(r1[1], r2[1])
    y2 = max(r1[1], r2[1])

    print(x1, x2, y1, y2) 
    dx = 1 if x2 > x1 else 0
    dy = 1 if y2 > y1 else 0
    x = x1
    y = y1
    print(dx, dy, x, y)
    while x != x2 or y != y2:
        if grid.get(y, x) == ".":
            grid.set(y, x, "X")
            print("Going green", x, y)
        else:
            print("Not greening", x, y, grid.get(y, x))
        x += dx
        y += dy

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    grid = Grid(12, 12, ".")
    red = []
    for l in lines:
        col, row = (int(n) for n in l.split(","))
        red.append( (col, row) )

        grid.set(row, col, "#")
    for i in range(len(red) - 1):
        connect(grid, red[i], red[i+1])
    connect(grid, red[-1], red[0])

    for r in grid.data:
        print("".join(r))
    #max_area = -1
    #for r1 in red:
    #    for r2 in red:
    #        a = abs(r2[1] - r1[1] + 1) * abs(r2[0] - r1[0] + 1)
    #        print(r1, r2, a)
    #        if a > max_area:
    #            max_area = a
    #print(max_area)
