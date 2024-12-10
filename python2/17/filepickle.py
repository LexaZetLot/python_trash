import pickle

def saveDbase(filename, object):
    file = open(filename, 'wb')
    pickle.dump(object, file)
    file.close()

def loadDbase(filename):
    file = open(filename, 'rb')
    object = pickle.load(file)
    file.close()
    return object