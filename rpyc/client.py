import rpyc
import sys
import os
import time

MB = 1024 * 1024

path = './data/'
# change the ip if the sever is deployed on remote server
server_ip = '128.6.13.131'

client_upload_start = 0.0
client_download_end = 0.0


def upload(server, filename):

    with open(path+filename, "rb") as f:
        data = f.read()
        server.write(str(filename), data)


def download(server, filename):

    data = server.read(str(filename))
    with open(path + 'new_' + filename, "wb") as f:
        f.write(data)


def getTime(server):
    time_1, time_2 = server.getTime()
    return time_1, time_2

def test_speed(server_ip = '128.6.13.131', port = 3154):
	con_server = rpyc.connect(server_ip, port=3154)
	server = con_server.root
	# sever equals to the class 'MyServer' in the sever file

	filename = '7.txt'
	client_upload_start = float(time.time())
	t1 = float(time.time())
	upload(server, filename)
	t2 = float(time.time())
	download(server, filename)
	t3 = float(time.time())

	filepath = path + filename
	file_info = os.stat(filepath)
	file_size = float(file_info.st_size)

	print("test: ", client_download_end)

	upload_speed = file_size / MB / (t2-t1)
	download_speed = file_size / MB / (t3-t2)
	print("The upload speed is: ", upload_speed, "MB/s")
	print("The download speed is: ", download_speed, "MB/s")
	return upload_speed,download_speed

