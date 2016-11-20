#Simple and easy multithreaded python server for testing network speeds. Must be running on target machine.


import socket
from thread import *

HOST = ''
PORT = 3333
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

def clientthread(conn):
    while 1:
        conn.recv(1024*10)

s.listen(10)
while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    start_new_thread(clientthread ,(conn,))
s.close()




