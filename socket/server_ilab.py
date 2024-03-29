import socket
import os
import sys
import struct
import time

MB = 1024 * 1024

def socket_service_connect():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('128.6.4.102', 3142))
        s.listen(1)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    server_path = "/ilab/users/wl497/speedtest/data/" # choose the dir path for local reciever

    print("Wait for Connection.....................")

    while True:
        sock, addr = s.accept()
        print("Accept connection from {0}".format(addr))
        time_1 = server_download_image(sock, server_path)
        time_2 = float(time.time())
        time_3 = server_upload_image(sock, server_path)

        # filepath = server_path + '2.jpg'
        # file_info = os.stat(filepath)
        # file_size = float(file_info.st_size)

        # upload_latency = time_2 - time_1
        # download_latency = time_3 - time_2

        # upload_speed = file_size / MB / upload_latency
        # download_speed = file_size / MB / download_latency

        # print("The upload speed on server side is: ", upload_speed, "MB/s")
        # print("The download speed on server side is: ", download_speed, "MB/s")

        sock.close()

def server_download_image(sock, path):

    fileinfo_size = struct.calcsize('128sq')
    buf = sock.recv(fileinfo_size)
    if buf:
        filename, filesize = struct.unpack('128sq', buf)
        fn = filename.decode().strip('\x00')
        new_filename = os.path.join(path, fn)  

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

    server_download_end_time = float(time.time())
    return server_download_end_time

def server_upload_image(sock, path):

    filepath = path + '2.jpg'
    fhead = struct.pack(b'128sq', bytes(os.path.basename(filepath), encoding='utf-8'), os.stat(filepath).st_size)
    
    upload_start_time = float(time.time())

    sock.send(fhead)

    fp = open(filepath, 'rb')
    while True:
        data = fp.read(1024)
        if not data:
            print('{0} send over...'.format(filepath))
            break
        sock.send(data)

    return upload_start_time


        
if __name__ == '__main__':
    socket_service_connect()
