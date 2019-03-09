path = "hightemp.txt"
count = 0

with open(path) as f:
    for line in f:
        count += 1

print(count)