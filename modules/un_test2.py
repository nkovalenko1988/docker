#!/usr/bin/env python

import mmap



with open("../logs/catalina.out", "r") as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    while True:
        line = m.readline()
        if line == '':
            break
        if "Undeploy" in str(line):
            print(line.rstrip())