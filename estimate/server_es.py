import socket
import time
import numpy as np
HOST ='IP address'
PORT = 3142                 #
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

print('Connected by', addr)
connecttime=time.time()
inter=10
time1=[]
i=0
while 1:
    data = conn.recv(1024)
    if data!=None:
        print(str(data))
        time1.append(float(time.time()))
        i+=1
    if(i>=2):
        break
inter=time1[1]-time1[0]
conn.sendall(str(inter).encode())
conn.close()
