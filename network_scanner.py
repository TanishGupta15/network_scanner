import scapy.all as scapy
import optparse
from auto import *


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP/ IP range.")
    parser.add_option("-i", "--interface", dest="interface", help="Interface that needs to be scanned")
    # Added a couple of help options
    (options, arguments) = parser.parse_args()
    if (not options.target) and (not options.interface):
        # Insufficient arguments
        return 0
    if not options.target:
        # Let's go through the interface
        ip = auto(options.interface)
        if ip == 0 or ip == 1:
            print("[-] Couldn't read the IP")
            return 0
        else:
            # Extracting the ip address of the broadcast
            # Example: If the src ip is 10.0.2.6, the broadcast_ip will look like: 10.0.2.1/24
            broadcast_ip = ""
            count = 0
            for i in ip:
                if i == '.':
                    broadcast_ip = broadcast_ip + i
                    count = count + 1
                    continue
                if count == 3:
                    broadcast_ip = broadcast_ip + "1/24"
                    # Refer readme for the significance of 1/24
                    return scan(broadcast_ip)
                broadcast_ip = broadcast_ip + i
    else:
        # if both specified or one specified, then go for target
        return scan(options.target)


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # Sends a request - "Who has the IP address = ip?"
    # pdst sets the destination ip we are looking for
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # dst sets the mac addresses that we want to target. ff:ff:ff:ff:ff:ff indicates that broadcast to all
    arp_request_broadcast = broadcast/arp_request
    # A combined package of both. Use .show() for details
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # srp = send and receive packets. verbose is set to false: don't print useless information.
    # Only accessing 0th element i.e. the answered list. 1st element is the unanswered list
    # Answered list contains the list of all IP addresses that were responded. It has many components.
    # Try .show() or .summary() for more details
    clients_list = []  # a list of dictionaries for every user(client)
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        # psrc contains the ip of the client and hwsrc contains its mac
        # To know all this, just use .summary() or .show() function of scapy
        clients_list.append(client_dict)  # We are forming a list of dictionaries
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


def run():
    args = get_arguments()
    if args == 0:
        print("[-] Please specify correct/sufficient arguments!")
    else:
        print_result(args)


run()
