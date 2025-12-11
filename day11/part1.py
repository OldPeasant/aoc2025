import sys


def count_paths(conn, path, current):
    if current == "out":
        return 1
    s = 0
    for n in conn[current]:
        if n not in path:
            path.append(n)
            s += count_paths(conn, path, n)
            path.pop()
    return s

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    conn = {}
    for l in lines:
        cell, outs_str = l.split(": ")
        outs = outs_str.split(" ")
        if cell in conn:
            raise Exception()
        conn[cell] = outs
        if cell in outs:
            print("SELF REF")
    print(conn)

    result = count_paths(conn, [], "you")
    print(result)
