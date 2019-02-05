#!/usr/bin/env python

with open('counties.csv', 'r') as f:
    for line in f.xreadlines():
        line = line.strip()
        if not line:
            continue
        fips, name = line.split(',')
        fips = int(fips)
        state_fips = fips // 1000
        print name, fips, state_fips
