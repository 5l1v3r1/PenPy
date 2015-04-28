#!/usr/bin/env python

from socket import *

if __name__ == '__main__':
    remote = input('Enter a website name:')
    remoteIP = gethostbyname(remote)

    print("scanning at "), remoteIP

    for i in range(20, 1025):
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((remoteIP, i))

        if result == 0:
            print('port %d: open' % (i,))

            s.close()