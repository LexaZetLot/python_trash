def countChar(name_file):
    name_file.seek(0)
    str_arr = name_file.read()
    return len(str_arr)

def countLines(name_file):
    name_file.seek(0)
    str_arr = name_file.read().split('\n')
    return len(str_arr)

if __name__ == '__main__':
    fp = open('test')
    print(countChar(fp))
    print(countLines(fp))