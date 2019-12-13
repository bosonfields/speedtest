from dns import resolver
import sys
import os
from latency import *


def resolver_addr(dnsserver, domain):
    res = resolver.Resolver()
    res.nameservers = dnsserver

    answers = res.query(domain)
    retval = []
    for d in answers:
        retval.append(d.address)
    return retval

def getDNS():

    domain_list = ['google.com', 'rutgers.edu',
                   'github.com', 'stackoverflow.com', 'wikipedia.org']
    dnsserver_list = ['8.8.8.8', '1.1.1.1', '9.9.9.9', '223.5.5.5']

    print('')
    print('')
    print('')
    print('DNS\Domain', end='\t\t')
    for domain in domain_list:
        print(domain, end='\t')
    print('')
    info=[]
    item=[]
    for dnsserver in dnsserver_list:
        print(dnsserver, end='\t\t\t')
        if len(dnsserver) < 9:
            print('\t', end='')
        item=[]
        item.append(dnsserver)
        for domain in domain_list:

            ip = resolver_addr([dnsserver], domain)
            # print(domain,dnsserver)

            ip = ip[0]
            latency = ping(ip)
            print(latency, 'ms', end='\t\t')
            item.append(latency)
        info.append(item)

        print('')

    print('')
    print('')
    print('')
    print(info)
    return info
