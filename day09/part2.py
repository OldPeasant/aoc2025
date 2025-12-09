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
    r = r1
    dx = si
    while r[0] != r2[0] and r[1] != r2[1]:
        r 
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
        print(r)
    #max_area = -1
    #for r1 in red:
    #    for r2 in red:
    #        a = abs(r2[1] - r1[1] + 1) * abs(r2[0] - r1[0] + 1)
    #        print(r1, r2, a)
    #        if a > max_area:
    #            max_area = a
    #print(max_area)
