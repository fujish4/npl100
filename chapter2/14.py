N = int(input('N-->'))

with open('hightemp.txt') as f:
    for i, line in enumerate(f):
        if i >= N:
            break
        print(line.rstrip())