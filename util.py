''' Utility functions '''

import urllib.request
import wmi
# import pypiwin32


def get_nic_input(configs):
    ''' Get NIC input from user and prints the name of the same'''

    selected_nic = None
    print('\nPlease select an NIC adapter: \n')
    while selected_nic is None:
        try:
            selected_nic = int(input()) - 1
        except ValueError:
            print(
                'Invalid input, please enter an integer between 1-{0}'.format(len(configs)))
            selected_nic = None
        if selected_nic < 0 or selected_nic > len(configs):
            print(
                'Invalid input, please enter an integer between 1-{0}'.format(len(configs)))
            selected_nic = None

    print_nic_name(configs[selected_nic])
    return selected_nic


def print_nic_list(configs):
    ''' Prints NIC names from the config list '''

    for index, config in enumerate(configs):
        name = config.Description
        print('{0}: {1}'.format(index + 1, name))


def print_nic_name(config):
    ''' Prints NIC name from the config '''

    name = config.Description
    print('\nTarget NIC: {0}\n'.format(name))


def get_nic_name(config):
    ''' Returns NIC name from the config '''

    name = config.Description
    return name


def get_nic_list():
    ''' Obtain network adaptors configurations '''

    configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    return configs


def is_connected():
    ''' Check if internet connection is working '''

    try:
        with urllib.request.urlopen('https://duckduckgo.com') as req:
            return req.status == 200
    except:
        return False


def reset_nic(index):
    ''' Reset network adapter to use DHCP'''

    nic_configs = get_nic_list()
    nic = nic_configs[index]

    # Enable DHCP
    nic.EnableDHCP()
