#!/usr/bin/env python

import urllib, sys

try:
    x = urllib.urlopen('http://') + sys.arg[1] + '/admin.php'
    print(x.read())
except:
    print('Not Found'