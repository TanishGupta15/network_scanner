# Network Scanner

A simple python script to scan all the devices on same network interface.

Run this script in linux environment to scan all the devices on your network interface. Catch your neighbors using your Wi-fi ;)

In terminal, type "python network_scanner.py --help" to get different arguments that can be used.

Commands: 

    1. python network_scanner.py --interface your_interface 
    
        where your_interface is the interface over which you want to scan.
        
    2. python network_scanner.py --target target_ip
    
        where target_ip is an IP address that you want to target
        
 
I have used 4 python modules:

    1. Subprocess - To execute terminal commands from python script

    2. optparse - To read command-line arguments

    3. re - To identify IP address using regular expressions
    
    4. scapy - To scan the networks and get information about them
    
    
About Network Scanning:

     When interface is specified, I have scanned over the range 10.x.y.1/24 for Ethernet connections and 192.168.x.1/24 for Wireless connections.
     
     So, for example, if the interface is eth0 and your IP is 10.0.2.6, I scan over from 10.0.2.1 to 10.0.2.255.
