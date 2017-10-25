''' IP scheduler '''

import sys
import time

# Import utility functions
UTILITIES = __import__('util')


def start(nic_index):
    ''' Starting the IP shifting... '''

    while True:
        print('Enter an IP address: ')
        ip_address = input()
        set_ip_address(nic_index, ip_address)
        time.sleep(5)
        if UTILITIES.is_connected():
            print('Connection seems good, waiting... \n')


def set_ip_address(nic_index, ip_address):
    ''' Initialize ip shifting mechanism on provided NIC '''

    nics = UTILITIES.get_nic_list()
    nic = nics[nic_index]

    try:
        nic.EnableStatic(IPAddress=[ip_address])
    except:
        print('Doh... Some unexpected error occured!')
        sys.exit(0)
