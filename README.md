# speedtest

## Testing with python socket
+ Set server_ilab.py on the remote server 
+ Set client_ilab.py on the local client 
+ Change the IP address with the server IP, and the path for test file. 

## Testing with python rpyc
+ Set server_rpyc.py on the remote server
+ Change the path and Ip address in client.py
+ Run the speedTest.py

+ //Currently, our private server is not maintained.

## Bandwidth Estimation
+ set server_es.py on the remote server
+ change the Ip address in the client_es.py
+ change the maximum bandwidth with maximum result from above test
+ Implement the client_es.py locally

## dns test
```c
pip install dnspython
pip install dnspython3
pip install netifaces
```
replace set_dns_mac() with set_dns_windows() if running in windows
