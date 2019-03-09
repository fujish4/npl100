path = "hightemp.txt"
count = 0
col1 = []
col2 = []
col3 = []
col4 = []

with open(path) as f,open('col1.txt', mode='w') as col1, open('col2.txt', mode='w') as col2:
    for line in f:
        cols = line.split('\t')
        col1.write(cols[0] + '\n')
        col2.write(cols[1] + '\n')
    
