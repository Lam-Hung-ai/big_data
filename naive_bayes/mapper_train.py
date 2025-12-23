#! /usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    elements = line.split(",")
    if len(elements) != 5:
        continue

    for i, element in enumerate(elements):
        if i != len(elements) -1:
            print(f"{elements[-1]}_col:{i}\t{element}")