#!/usr/bin/env python
__author__ = 'byt3smith'

from util.commands import *
from util.cli import CLI
from util.output import *
from platform import system
import os
import yaml
import getpass
import argparse

# Logo for console
def logo():
    banner = """
     _______._________.      _____.
    ( ______|____  \\| |     (_____ \\
    | |      ____)  ) |      _____) )
    | |     |  __  (| |     |  __  /
    | |_____| |__)  ) |_____| |  \\ \\
    \\_______)______/|_______)_|  |_|
    CarbonBlack Live Response Console v.1
    """

    os_tag = system()
    if os_tag == 'Linux' or os_tag == 'Darwin':
      os.system('clear')
    elif os_tag == 'Windows':
      os.system('cls')
    print cyan(banner.center(100))


def addtoconf(yamlstr, servid):
    newserv = raw_input("\n[*] CB Server URL (https://cb.server) : ")
    yamlstr['server'][servid] = newserv
    return newserv


################
# Main Console #
################
class Console(object):

    def __init__(self):
        # This will keep the main loop active as long as it's set to True.
        self.active = True

    def stop(self):
        # Stop main loop.
        self.active = False

    def start(self, url, token, log):
        cli = CblrCli(url, token, log)
        # Main loop.
        while self.active:
            cli.prompt = cyan('cblr ') + '> '
            cli.cmdloop()


if __name__ == '__main__':
    ### CLI argument declaration
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-log", type=str, nargs='?', default='http_cblr.log', help='Specify file to log HTTP transactions. Default is http_cblr.log')

    # Parse command-line arguments
    args = parser.parse_args()

    # Get config from conf.yml
    stream = file('conf.yml', 'r')
    yamlstr = yaml.load(stream)

    logo()  # prints out logo

    host = yamlstr['server']
    if host is None:
        newserv = raw_input("[*] CB Server URL (https://cb.server): ")
        server = {1: newserv}
        yamlstr['server'] = server
        host = newserv
    else:
        hostlen = len(host)
        serverList = []
        for i in range(1, hostlen+1):
            serverList.append([i, yamlstr['server'][i]])
        print "Available Live Response Servers"
        print table(['ID', 'Server URL'], serverList)
        choice = int(raw_input("\n[1-%d] or 0 to add new > " % hostlen))
        while choice > hostlen:
            print "Incorrect option.. Try again"
            choice = raw_input('[1-%d] > ' % hostlen)
        if choice == 0:
            host = addtoconf(yamlstr, hostlen+1)
        else:
            host = yamlstr['server'][choice]

    username = raw_input("\n[*] CB Username: ")
    try:
        token = yamlstr['apitokens'][username]
    except:
        token = getpass.getpass('[*] API token for %s (will not be echoed): ' % username)

    yamlstr['apitokens'][username] = token
    stream = file('conf.yml', 'w')
    yaml.dump(yamlstr, stream)

    # Start console!
    Console().start(host, token, args.log)
