#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list= scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        client_dict = {"ip":element[1].psrc ,"MAC Address":element[1].hwsrc}
        clients_list.append(client_dict)      
    return clients_list
    #print(answered_list.summary())
    #print(arp_request.summary())
    #scappy.ls(function name) - lists all the fields which we can set to a function

def print_result(result_list):
    print("--------------------------------------------------------------------------------------")
    print("IP\t\t\tMAC Address")
    print("--------------------------------------------------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["MAC Address"])


scan_result=scan("10.0.2.1/24")
print_result(scan_result)
