# speedtest

## Testing with python socket
set server_ilab.py on the remote server
set client_ilab.py on the local client
Change the IP address with the server IP, and the path for test file.

## Testing with python rpyc
set server_rpyc.py on the remote server
change the path and Ip address in client.py
run the speedTest.py

//Currently, our private server is not maintained.

## Bandwidth Estimation
set server_es.py on the remote server
change the Ip address in the client_es.py
change the maximum bandwidth with maximum result from above test
implement the client_es.py locally

## dns test

pip install dnspython
pip install dnspython3
pip install netifaces

replace set_dns_mac() with set_dns_windows() if running in windows
