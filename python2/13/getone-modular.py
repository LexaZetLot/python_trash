import getfile
from getpass import getpass
filename = 'monkeys.jpg'


getfile.getfile(file=filename,
                site='ftp.rmi.net',
                dir ='.',
                user=('lutz', getpass('Pswd?')),
                refetch=True)


if input('Open file?') in ['Y', 'y']:
    from playfile import playfile
    playfile(filename)