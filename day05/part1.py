import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    ranges = []
    ids = []

    in_ranges = True
    for l in lines:
        if len(l) > 0:
            if in_ranges:
                ranges.append(list(int(b) for b in l.split("-")))
            else:
                ids.append(int(l))
        else:
            in_ranges = False
    count_fresh = 0
    for id in ids:
        is_fresh = False
        for r in ranges:
            if id >= r[0] and id <= r[1]:
                is_fresh = True
                break
        if is_fresh:
            count_fresh += 1
    print(count_fresh)
