import socket
import os
import sys
import struct
import time

MB = 1024 * 1024

def socket_client_connect():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        path = '128.6.4.103'
        port = 3142
        s.connect((path, port))  
    except socket.error as msg:
        print(msg)
        print(sys.exit(1))

    client_path = '/data/' # you can change your path

    client_upload_start_time = client_upload_image(s, client_path)
    client_mid_time = float(time.time())
    client_download_end_time = client_download_image(s, client_path)

    filepath = client_path + '2.jpg'
    file_info = os.stat(filepath)
    file_size = float(file_info.st_size)

    upload_latency = client_mid_time - client_upload_start_time
    download_latency = client_download_end_time - client_mid_time

    upload_speed = file_size / MB / upload_latency
    download_speed = file_size / MB / download_latency

    print("The remote server is built on ilab")
    print("The test file size is: ", file_size / MB, "MB")
    print("The upload speed on client side is: ", upload_speed, "MB/s")
    print("The download speed on client side is: ", download_speed, "MB/s")

    s.close()

    return upload_speed, download_speed

def client_upload_image(s, path):

    filepath = path + '2.jpg' # choice your own image for testing

    fhead = struct.pack(b'128sq', bytes(os.path.basename(filepath), encoding = 'utf-8'), os.stat(filepath).st_size)
    
    upload_start_time = float(time.time())

    s.send(fhead)

    fp = open(filepath, 'rb')
    while True:
        data = fp.read(1024)
        if not data:
            print('{0} send over...'.format(filepath))
            break
        s.send(data)

    return upload_start_time
    terminateSocket(s)

def terminateSocket(s):
    s.close()

# def getEstimate(s, maxband):
#     s.sendall('Test1!'.encode())
#     time.sleep(0.5)
#     s.sendall('Test2!'.encode())
#     data = s.recv(1024)
#     band=maxband*(1-((float(data)-0.5)/0.5))
#     return band

def client_download_image(sock, path):

    fileinfo_size = struct.calcsize('128sq')
    buf = sock.recv(fileinfo_size)
    if buf:
        filename, filesize = struct.unpack('128sq', buf)
        fn = filename.decode().strip('\x00')
        new_filename = os.path.join(path, 'new_' + fn)

        recvd_size = 0
        fp = open(new_filename, 'wb')

        while not recvd_size == filesize:
            if filesize - recvd_size > 1024:
                data = sock.recv(1024)
                recvd_size += len(data)
            else:
                data = sock.recv(1024)
                recvd_size = filesize
            fp.write(data)
        fp.close()

    download_end_time = float(time.time())
    return download_end_time
   
if __name__ == '__main__':
    up, down = socket_client_connect()
