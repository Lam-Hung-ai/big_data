#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
current_files = set()

for line in sys.stdin:
    line = line.strip()
    
    try:
        word, filename = line.split('\t', 1)
    except ValueError:
        continue

    if current_word == word:
        current_count += 1
        current_files.add(filename)
    else:
        if current_word:
            files_str = ",".join(sorted(current_files))
            print(f"{current_word}\t{current_count}\t{files_str}")
        
        current_word = word
        current_count = 1
        current_files = {filename}

if current_word:
    files_str = ",".join(sorted(current_files))
    print(f"{current_word}\t{current_count}\t{files_str}")

