#!/usr/bin/env python3
import sys
import os

filepath = os.environ.get("mapreduce_map_input_file", "Unknown")
filename = os.path.split(filepath)[-1]

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    
    for word in words:
        print(f"{word}\t{filename}")
