#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(",")
    
    if len(parts) != 4 or parts[0] == "Year":
        continue
        
    year = parts[0]
    faculty = parts[2]
    amount = parts[3]
    
    print(f"{year}_{faculty}\t{amount}")