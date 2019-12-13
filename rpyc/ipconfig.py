import os
# Routing Gateway,Routing NIC Name,Routing NIC MAC Address,Routing IP Address,Routing IP Netmask


def ipconfig():
    import netifaces

    routingGateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
    routingNicName = netifaces.gateways()['default'][netifaces.AF_INET][1]

    for interface in netifaces.interfaces():
        if interface == routingNicName:
            routingNicMacAddr = netifaces.ifaddresses(
                interface)[netifaces.AF_LINK][0]['addr']
            try:
                routingIPAddr = netifaces.ifaddresses(
                    interface)[netifaces.AF_INET][0]['addr']
                routingIPNetmask = netifaces.ifaddresses(
                    interface)[netifaces.AF_INET][0]['netmask']
            except KeyError:
                pass
    return [routingGateway, routingNicName, routingNicMacAddr, routingIPAddr, routingIPNetmask]


def set_dns_windows(dns_server):
    command = 'netsh interface ip set dns name="WLAN" source=static addr=' + \
        str(dns_server)
    os.system(command)


def set_dns_mac(dns_server):
    command = 'networksetup -setdnsservers Wi-Fi ' + str(dns_server)
    os.system(command)


# set_dns_mac('8.8.8.8')
#
# info = ipconfig()
# print('Default Gateway:', info[0])
# print('MAC Address:', info[2])
# print('IPv4 Address:', info[3])
# print('Subnet Mask:', info[4])
