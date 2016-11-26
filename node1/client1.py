import socket
import sys
import os

def Main():

    connected = True

    port = 9001
    host = socket.gethostname()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    s.connect((host, port))
    
    while connected:

        cmd = raw_input('node1:~$ ')
        s.send(cmd)

        if cmd == 'quit':

            print 'client| user quit'
            break

        else:

            args = cmd.split()
            
            if args[0] == 'IndexGet':
        
                listdir = s.recv(1024)
                print listdir

            if args[0] == 'FileDownload':

                filename = args[1]

                with open(filename, 'wb') as f:

                    print 'client| file opened'

                    data = s.recv(1024)

                    f.write(data)

                f.close()
                print 'client| file received'

            if args[0] == 'FileHash':

                data = s.recv(1024)

                print 'client| ' + data

    s.close()
    print 'client| connection closed'

if __name__ == '__main__':
	Main()
