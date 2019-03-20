with open("hightemp.txt") as f:
    lines = f.readlines()
    lines.sort(key= lambda line: float(line.split("\t")[2]), reverse=True)

for line in lines:
    print(line.strip())