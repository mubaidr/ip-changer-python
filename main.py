''' IP Changer Module '''

import sys
import signal
from win32com.shell import shell
# Import scheduler functions
SCHEDULER = __import__('scheduler')
# Import utility functions
UTILITIES = __import__('util')


def signal_handler(signal, frame):
    ''' Handles the program exit '''

    global SELECTED_NIC
    UTILITIES.reset_nic(SELECTED_NIC)
    print('Bye Bye!')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

if shell.IsUserAnAdmin() != True:
    print('\nI hate non-admin users! (-_- )\n')
    sys.exit(0)
else:
    # Welcome message
    print('\nHello!\n')
    print('   ;')
    print('  /_\\')
    print('\\(o.o)')
    print('  ) (\\')
    print('  / \\\n\n')

    # Collect system NICs
    NIC_CONFIGS = UTILITIES.get_nic_list()
    # Print system NICs
    UTILITIES.print_nic_list(NIC_CONFIGS)
    # Get target NIC from user
    SELECTED_NIC = UTILITIES.get_nic_input(NIC_CONFIGS)
    # start the process
    SCHEDULER.start(SELECTED_NIC)
