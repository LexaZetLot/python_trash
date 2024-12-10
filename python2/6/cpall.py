import os, sys

maxfileload = 1000000
blksize = 1024 * 500


def copyfile(pathFrom, pathTo, maxfileload=maxfileload):
    if os.path.getsize(pathFrom) <= maxfileload:
        bytesFrom = open(pathFrom, 'rb').read()  # read small file all at once
        open(pathTo, 'wb').write(bytesFrom)
    else:
        fileFrom = open(pathFrom, 'rb')  # read big files in chunks
        fileTo = open(pathTo, 'wb')  # nned b mode for both
        while True:
            bytesFrom = fileFrom.read(blksize)  # get one block, less at end
            if not bytesFrom: break  # empty after last chunk
            fileTo.write(bytesFrom)


def copytree(dirFrom, dirTo, verbose=0):
    fcount = dcount = 0
    for filename in os.listdir(dirFrom):
        pathFrom = os.path.join(dirFrom, filename)
        pathTo = os.path.join(dirTo, filename)  # extend both paths
        if not os.path.isdir(pathFrom):  # copy simple files
            try:
                if verbose > 1: print('copying', pathFrom, 'to', pathTo)
                copyfile(pathFrom, pathTo)
                fcount += 1
            except:
                print('Error copying', pathFrom, 'to', pathTo, '--skipped')
                print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            if verbose: print('copying dir', pathFrom, 'to', pathTo)
            try:
                os.mkdir(pathTo)
                below = copytree(pathFrom, pathTo)
                fcount += below[0]
                dcount += below[1]
                dcount += 1
            except:
                print('Error creating', pathTo, '--skipped')
                print(sys.exc_info()[0], sys.exc_info()[1])
    return (fcount, dcount)


def getargs():
    try:
        dirFrom, dirTo = sys.argv[1:]
    except:
        print('Usage error: cpall.py dirFrom dirTo')
    else:
        if not os.path.isdir(dirFrom):
            print('Error: dirFrom is not a directory')
        elif not os.path.exists(dirTo):
            os.mkdir(dirTo)
            print('Note: dirTo was created')
            return (dirFrom, dirTo)
        else:
            print('Warning: dirTo already exists')
            if hasattr(os.path, 'samefile'):
                same = os.path.samefile(dirFrom, dirTo)
            else:
                same = os.path.abspath(dirFrom) == os.path.abspath(dirTo)
            if same:
                print('Error: dirFrom same as dirTo')
            else:
                return (dirFrom, dirTo)


if __name__ == '__main__':
    import time

    dirstuple = getargs()
    if dirstuple:
        print('Copying...')
        start = time.clock()
        fcount, dcount = copytree(*dirstuple, verbose=2)
        print('Copied', fcount, 'files', dcount, 'directories', end=' ')
        print('in', time.clock() - start, 'seconds')