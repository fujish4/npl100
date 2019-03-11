with open('col1.txt') as col1_file, \
        open('col2.txt') as col2_file, \
        open('merge.txt', mode='w') as out_file:

    for col1, col2 in zip(col1_file, col2_file):
        out_file.write(col1.rstrip() + "\t" + col2.rstrip() + "\n")