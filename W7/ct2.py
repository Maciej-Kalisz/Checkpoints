tally = {"total": 0}

with open("shakespeare.txt") as f:
    for line in f:
        for c in line.replace(" ", ""):
            if c.isalpha():
                tally["total"] += 1
                c = c.upper()
                if c in tally:
                    tally[c] += 1
                else:
                    tally[c] = 1

total = tally["total"]

keys = list(tally.keys())
keys.sort()

sorted_tally = {i: tally[i] for i in keys}

for l, f in sorted_tally.items():
    if l == "total":
        continue

    print(f"{l} appears {f} times ( {(f/total) * 100} % )")
