path = "hightemp.txt"
count = 0

with open(path) as f:
    l = f.read()
    print(l.replace('\t', ' '))

