import socket
import time
HOST = 'IP address'
PORT = 3154
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

maxband= 8.27  # replace with result from network test
s.sendall('Test1!'.encode())
print('Test1!'.encode())
time.sleep(0.05)
s.sendall('Test2!'.encode())
data = s.recv(1024)
print(data)
band=maxband*(1-((float(data)-0.05)/0.05))
s.close()
print ('bandwidth', band)
