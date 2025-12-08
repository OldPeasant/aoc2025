import sys

with open(sys.argv[1]) as f:
    ranges = {}
    for l in f.read().splitlines():
        if len(l) == 0:
            break
        lower, higher = list(int(b) for b in l.split("-"))
        ranges[lower] = ranges.get(lower, 0) + 1
        ranges[higher+1] = ranges.get(higher + 1, 0) - 1
    count_fresh = 0
    current_start = None
    height = 0
    for r in sorted(ranges.keys()):
        height += ranges[r]
        if current_start is None and height > 0:
            current_start = r
        if current_start is not None and height == 0:
            count_fresh += r - current_start
            current_start = None
    print(count_fresh)
