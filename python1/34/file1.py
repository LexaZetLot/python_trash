with open('data') as fin, open('res', 'w') as fout:
    for line in fin:
        fout.write(line)