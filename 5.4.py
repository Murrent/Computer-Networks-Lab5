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
DNS_server = '8.8.8.8'
DNS_port = 53
timeout = 5
# -----------------------------------------
# Socket initialization
# -----------------------------------------

clientsocket = socket(AF_INET, SOCK_DGRAM)  # SOCK_DGRAM for UDP
clientsocket.settimeout(timeout)

DNS_port = int(DNS_port)

url_to_query = 'bbc.co.uk'
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

    msgLength = len(message)  # saving length
    index = 18 + len(url_to_query)  # offset to beginning of the first answer
    while index < msgLength:  # loop while inside string length
        if message[index + 2] == 0 and message[index + 3] == 1:  # Check if answer is of type A
            messageIP = ""  # Create empty string
            for i in range(message[index + 11]):  # loop over the IP's length
                messageIP += str(message[index + 12 + i])  # add the next byte to the address
                if i != int(message[index + 11] - 1):  # if we are no at the end of the address
                    messageIP += "."  # add a "." to the end of the string
            print(messageIP)  # print the IP

        index += 12 + message[index + 11]  # jump to next answer by updating the index

    # -----------------------------------------

except:
    # -----------------------------------------
    # Exception handling
    # -----------------------------------------
    print('A timeout has occured, no reply from the DNS server')
