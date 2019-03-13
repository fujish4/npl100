N = int(input('N-->'))
with open('hightemp.txt') as f:
    lines = f.readlines()

count = len(lines)
unit = count // N

for i, start in enumerate(range(0, count, unit), 1):
    with open('child_{0}.txt'.format(i), mode='w') as out:
        for line in lines[start:start+unit]:
            out.write(line)

