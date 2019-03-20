from itertools import groupby

with open("hightemp.txt") as f:
    col1 = [ line.split("\t")[0] for line in f.readlines() ]

col1.sort()
result = [ (c, len(list(group))) for c, group in groupby(col1) ]

result.sort(key= lambda c: c[1], reverse=True)

for r in result:
    print('{}({})'.format(r[0], r[1]))