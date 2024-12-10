#while True:
#    reply = input('Enter a number: ')
#    if reply == 'stop':
#        break
#    elif not reply.isdigit():
#        print('Bad!' * 8)
#    else:
#        num = int(reply)
#        if num < 20:
#            print('low')
#        else:
#            print(num ** 2)
#print("Bye")

while True:
    reply = input("Enter a number: ")
    if reply == 'stop': break
    try:
        print(float(reply) ** 2)
    except:
        print("Invalid input")
print('Bye')