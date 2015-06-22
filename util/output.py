# This file is part of Viper - https://github.com/botherder/viper
# See the file 'LICENSE' for copying permission.

import os
import sys
from prettytable import PrettyTable
from colorama import Fore, init

##################### COLORIZER ###################################

init(autoreset=True)

def red(text, readline=False):
    return Fore.RED + text + Fore.RESET

def green(text, readline=False):
    return Fore.GREEN + text + Fore.RESET

def yellow(text, readline=False):
    return Fore.YELLOW + text + Fore.RESET

def blue(text, readline=False):
    return Fore.BLUE + text + Fore.RESET

def magenta(text, readline=False):
    return Fore.MAGENTA + text + Fore.RESET

def cyan(text, readline=False):
    return Fore.CYAN + text + Fore.RESET

def white(text, readline=False):
    return Fore.WHITE + text + Fore.RESET

def bold(text, readline=False):
    return Fore.BRIGHT + text + Fore.RESET


############################## STDOUT ################################

def print_info(message):
    print(bold(cyan("[*]")) + " {0}".format(message))

def print_item(message, tabs=0):
    print(" {0}".format("  " * tabs) + cyan("-") + " {0}".format(message))

def print_warning(message):
    print(bold(yellow("[!]")) + " {0}".format(message))

def print_error(message):
    print(bold(red("[!]")) + " {0}".format(message))

def print_success(message):
    print(bold(green("[+]")) + " {0}".format(message))

def table(header, rows):
    table = PrettyTable(header)
    table.align = 'l'
    table.padding_width = 1

    for row in rows:
        table.add_row(row)

    return table
