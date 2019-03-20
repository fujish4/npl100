with open("hightemp.txt") as f:
    ken = set()
    for line in f:
        cols = line.split("\t")
        ken.add(cols[0])

for k in ken:
    print(k)