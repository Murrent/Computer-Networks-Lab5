# Martin Vickgren

# -----------------------------------------------------------
# -----------------------------------------------------------
# Lab 5: DNS client
# General structure
# -----------------------------------------------------------
# -----------------------------------------------------------
import sys, time, msgFunctions
from socket import *


def formatURL(url_in):
    return msgFunctions.attach12(msgFunctions.formatNameFiled(url_in))  # reusing functions to format the URL


# DNS_server='10.1.112.11'
DNS_server = '130.243.97.77'
DNS_port = 53
timeout = 5
# -----------------------------------------
# Socket initialization
# -----------------------------------------

clientsocket = socket(AF_INET, SOCK_DGRAM)  # SOCK_DGRAM for UDP
clientsocket.settimeout(timeout)

DNS_port = int(DNS_port)

url_to_query = 'www.oru.se'
formatted_url = formatURL(url_to_query)
additional_info = b''
# -----------------------------------------
# Question assembly (YOUR CODE)
# -----------------------------------------
query_to_DNS = formatted_url + additional_info

try:

    clientsocket.sendto(query_to_DNS, (DNS_server, DNS_port))
    message, address = clientsocket.recvfrom(1024)

    # -----------------------------------------
    # Response parsing (YOUR CODE)
    # -----------------------------------------

except:
    # -----------------------------------------
    # Exception handling
    # -----------------------------------------
    print('A timeout has occured, no reply from the DNS server')
