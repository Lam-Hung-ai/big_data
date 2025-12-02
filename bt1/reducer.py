#!/usr/bin/env python3
import sys

current_key = None
current_sum = 0
current_count = 0
max_avg = 0
max_key = ""

for line in sys.stdin:
    line = line.strip()
    key, amount = line.split("\t")
    
    try:
        amount = float(amount)
    except ValueError:
        continue

    if current_key == key:
        current_sum += amount
        current_count += 1
    else:
        if current_key:
            avg = current_sum / current_count
            print(f"{current_key}\t{avg}")
            
            if avg > max_avg:
                max_avg = avg
                max_key = current_key
                
        current_key = key
        current_sum = amount
        current_count = 1

if current_key:
    avg = current_sum / current_count
    print(f"{current_key}\t{avg}")
    if avg > max_avg:
        max_avg = avg
        max_key = current_key

print("-" * 20)
print(f"HIGHEST: {max_key} with Average: {max_avg}")