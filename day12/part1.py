import sys

class Shape:
    def __init__(self, ix, lines):
        self.ix = ix
        self.lines = lines

    def rotate(self):
        new_lines = []
        for j in reversed(range(len(self.lines[0]))):
            new_line = []
            for i in range(len(self.lines)):
                new_line.append(self.lines[i][j])
            new_lines.append(new_line)
        return Shape(self.ix, new_lines)

    def as_text(self):
        rows = []
        rows.append(str(self.ix))
        for l in self.lines:
            rows.append("".join(l))
        return "\n".join(rows)

class Region:
    def __init__(self, line):
        grid_size, indexes = line.split(": ")
        self.width, self.height = (int(i) for i in grid_size.split("x"))
        self.indexes = list(int(i) for i in indexes.split(" "))

    def as_text(self):
        return str(self.width) + "x" + str(self.height) + ": " + " ".join(str(i) for i in self.indexes)

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    shapes = []
    curr_block = []
    for l in lines:
        if len(l) == 0:
            shapes.append(Shape(int(curr_block[0][:-1]), curr_block[1:]))
            curr_block = []
        else:
            curr_block.append(l)
        
    regions = list(Region(r) for r in curr_block)

    for s in shapes:
        print("===============================")
        print(s.as_text())
        print("")
        r = s
        for i in range(4):
            r = r.rotate()
            print(r.as_text())
    for r in regions:
        print(r.as_text())
