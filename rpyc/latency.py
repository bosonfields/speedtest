import os
import socket
import time
import select
import struct


ICMP_ECHO_REQUEST = 8


def checksum(source_string):
    sum = 0
    count = 0
    max_count = (len(source_string)/2)*2
    while count < max_count:
        thisVal = source_string[count + 1]*256 + source_string[count]
        sum = sum + thisVal
        sum = sum & 0xffffffff
        count = count + 2
    if max_count < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xffffffff
    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


def receive_ping(sock, id, timeout):
    time_left = timeout
    while True:
        starttime = time.time()
        readable = select.select([sock], [], [], time_left)
        wait_time = (time.time() - starttime)
        if readable[0] == []:
            return

        time_received = time.time()
        rcv_data, addr = sock.recvfrom(1024)
        icmp_header = rcv_data[20:28]  # icmp头部信息
        type, code, checksum, packetID, sequence = struct.unpack(
            "bbHHh", icmp_header
        )
        if type != 8 and packetID == id:
            bytesInDouble = struct.calcsize("d")
            time_sent = struct.unpack(
                "d", rcv_data[28:28 + bytesInDouble])[0]
            return time_received - time_sent

        time_left = time_left - wait_time
        if time_left <= 0:
            return


def send_ping(sock, dest_addr, id):
    dest_addr = socket.gethostbyname(dest_addr)
    checksum1 = 0
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, checksum1, id, 1)
    bytesInDouble = struct.calcsize("d")
    data = (192 - bytesInDouble) * "Q"
    data = struct.pack("d", time.time()) + data.encode()

    checksum1 = checksum(header + data)
    header = struct.pack(
        "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(checksum1), id, 1
    )
    packet = header + data
    sock.sendto(packet, (dest_addr, 1))


def do(dest_addr, timeout):
    icmp = socket.getprotobyname("icmp")
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    my_ID = os.getpid() & 0xFFFF
    send_ping(sock, dest_addr, my_ID)
    delay = receive_ping(sock, my_ID, timeout)
    sock.close()
    return delay


def ping(dest_addr, timeout=2, count=10):
    #print(u"ping {}...".format(dest_addr))
    lat = 0
    for i in range(count):
        delay = do(dest_addr, timeout)
        if delay == None:
            return -1
        else:
            delay = delay * 1000
            lat += delay
    return(round(lat/10, 2))


if __name__ == '__main__':
    print(ping('172.217.10.14'))
