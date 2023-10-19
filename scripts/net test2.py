import os
import ipaddress

host = ipaddress.ip_address(input("What host: "))

for ip in host:
    response = os.popen(f"ping -c 4 {ip} ")
    
    if("Request timed out." or "unreachable") in response:
        print(response)
        