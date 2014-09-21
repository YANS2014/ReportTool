# !/usr/bin/env Python
# -*- coding:utf-8 -*-

import sys
import json
import re

def main():
    if len(sys.argv) < 2 :
        print 'Usage: {0} input-file [output-file]'.format(sys.argv[0])
        sys.exit(1)

    src = sys.argv[1]
    text = ""
    with open(src) as fin:
        text = fin.read()


if __name__ == '__main__':
    main()

