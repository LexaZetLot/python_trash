def callback1(label, count):
    return 'callback1 => %s number %i' % (label, count)

def callback2(label, count):
    return 'callback2 => ' +  label * count


import cregister

print('\nTest1:')
cregister.setHandler(callback1)      
for i in range(3):
    cregister.triggerEvent()         

print('\nTest2:')
cregister.setHandler(callback2)
for i in range(3):
    cregister.triggerEvent()         