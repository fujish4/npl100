N = int(input())

with open('hightemp.txt') as f:
    lines = f.readlines()
    for line in lines[-N:]:
        print(line.rstrip())