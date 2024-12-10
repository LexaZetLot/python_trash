fp = open('input.txt', 'w')
fp.write("Hello file world!")
fp.close()

fp = open('input.txt', 'r')
print(fp.read() + '\n')

