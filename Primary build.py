# this is a pretty simple script used to get familiar with the socket library
# and its uses with scanning ports
# there will be a ridiculous amount of comments, you've been warned

# imports the socket module and everything within it, not great for computer
# memory granted, but at the time of writing this program, I don't know
# what will and won't be needed
from socket import *

# sys provides access to system specific functions, time is used to keep track
# of how long a port scan takes, datetime is the mechanism of this
import sys, time
from datetime import datetime


# need the host address, port to start at and port to stop at
host = ''
min_port = 1
max_port = 5

# asks for input in the form of a url address or a direct IP address
try:
    host = input('[*] Enter Target Host Address: ')
except KeyboardInterrupt:
    print('[*] User requested interruption')
    print('[*] System closing')
    sys.exit()

# next, we get the host by name, meaning we retrieve the IP address of the
# input url or if the input was a direct IP, we retrieve that all the same
hostIP = gethostbyname(host)

# gets the current time when the program runs, to be used later to determine
# overall runtime
t1 = datetime.now()


# scan_host function uses the socket function to try to connect to the target
def scan_host(ahost, aport, r_code=1):
    try:
        s = socket(AF_INET, SOCK_STREAM)

        code = s.connect_ex((ahost, aport))

        if code == 0:
            r_code = code
        s.close()
    except Exception:
        pass

    return r_code


# scanning, uses range function to iterate through all the ports we want,
# min and max port, and uses the scan_host function, with the parameters
# of the host ip address and the port in question of the IP, to determine
# if a port is open or not, if a 0 is returned, the port is open, else the
# port is closed
# some exception handling involved as well, if an error is thrown, pass allows
# the program to continue
try:
    for port in range(min_port, max_port):
        response = scan_host(host, port)

        if response == 0:
            print('[*] Port %d: Open' % port)
except Exception:
    pass

t2 = datetime.now()

total = t2-t1

print("Scan completed in: ", total)
