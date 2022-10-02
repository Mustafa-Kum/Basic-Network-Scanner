# pip install --pre scapy[basic]
import scapy.all as scapy
import optparse

def user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ipaddress", dest = "ip_address", help = "Enter IP adress")

    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ip_address:
        print("Enter Ip Address")
    
    return user_input


def Network_Scanner(ip):
    arp_request_packet = scapy.ARP(pdst = ip )
    #scapy.ls(scapy.ARP())

    broadcast_packet = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())

    combined_packet = broadcast_packet / arp_request_packet ## ---> Scapy dilinde bu iki paketi al tek paket yap.

    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout = 1)
    answered_list.summary()

user_ip_address = user_input()

Network_Scanner(user_ip_address.ip_address)
