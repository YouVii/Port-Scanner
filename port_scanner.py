import socket
import sys
import time

usage = "port_scanner.py TARGET START_PORT END_PORT"

print("_"*50)
print("Port Scanner")
print("_"*50)


if (len(sys.argv) != 4):
    print(usage)
    sys.exit()
try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()
            
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target", target)

for port in range(start_port, end_port+1):
    
    print("Scanning port:", port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    conn = s.connect_ex((target, port))
    if(not conn):
        print("port {} is OPEN".format(port))
    s.close()