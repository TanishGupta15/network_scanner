import subprocess
import re


# Please use this option only on Linux


def auto(interface):
    try:
        ifconfig_result = subprocess.check_output(["ip", "-4", "addr", "show", interface])
        # check the ip address of the host for given interface
    except:
        print("[-] Some error occured! Please try again!")
        return 1
    else:
        ip_search_result = re.search(r"(\d)*\.(\d)*\.(\d)*.(\d)*", ifconfig_result.decode('utf-8'))
        if ip_search_result:
            return ip_search_result.group(0)
            # Return first instance of the matching regex
        else:
            return 0
