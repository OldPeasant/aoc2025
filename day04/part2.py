import sys
import copy

def fewer(grid, row, col):
    if grid[row][col] == ".":
        return False
    ats = 0
    for d1 in range(-1, 2):
        for d2 in range(-1, 2):
            if not(d1 == 0 and  d2 == 0) and  grid[row + d1][col + d2] == "@":
                ats += 1
    return ats < 4

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    grid = []
    height = len(lines) + 2
    width = len(lines[0]) + 2
    grid.append(list(width * "."))
    for l in lines:
        grid.append(list("." + l + "."))
    grid.append(list(width * "."))
    grid_result = copy.deepcopy(grid)
    for g in grid:
        print(g)
    count = 0
    while True:
        has_removed = False
        for col in range(1, width - 1):
            for row in range(1, height - 1):
                print("check", row, col);
                if fewer(grid, row, col):
                    print("    yes")
                    count += 1
                    has_removed = True
                    grid[row][col] = "."
                    grid_result[row][col] = "x"
                else:
                    print("    no")
        if not has_removed:
            break
    for g in grid_result:
        print(g)
    print(count)
