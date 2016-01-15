#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from fcfs import *
from sjf import *
from rr import *

def main():
    # Carrega o arquivo em uma lista
    lines = sys.stdin.readlines()

    fcfs = FCFS(lines)
    sjf = SJF(lines)
    rr = RR(lines)

    print('FCFS', fcfs.output)
    print('SJF', sjf.output)
    print('RR', rr.output)

if __name__ == "__main__":
    main()
