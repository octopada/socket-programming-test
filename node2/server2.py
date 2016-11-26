import socket
import sys
import os
import hashlib  
import subprocess

def Main():

    args = []
    connected = True

    port = 9001
    host = socket.gethostname()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    s.listen(5)
    
    while True:

        cs, addr = s.accept()
        print("server| connected to {}".format(addr))

        while connected:

            cmd = cs.recv(1024)
            print('server| command received: {}'.format(cmd))

            if cmd == 'quit':

                print 'server| user quit'
                connected = False

            else:

                args = cmd.split()

                if args[0] == 'IndexGet':

                    listdir = os.listdir(".")
                    print 'server| sending listdir'

                    strdir = ''.join(str(x)+' ' for x in listdir)
                    cs.send(strdir)

                if args[0] == 'FileDownload':

                    filename = args[1];
                    f = open(filename, 'rb')
                    line = f.read(1024)
                    
                    cs.send(line)

                    f.close()
                    print 'server| done sending'

                if args[0] == 'FileHash':

                    if args[1] == 'verify':

                        cs.send(hashlib.md5(open(args[2], 'rb').read()).hexdigest())

                    elif args[1] == 'checkall':

                        allfiles = os.listdir('.')
                        afr = "".join(hashlib.md5(open(x, 'rb').read()).hexdigest() + ' ' + str(x) + '\n' for x in allfiles)
                        cs.send(afr)

        cs.close()
        print 'server| connection closed'

if __name__ == '__main__':
	Main()
