#!/usr/bin/env python3
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    try:
        # Tách Key và Value (Key ở đây bao gồm cả "Word,Label")
        line = line.strip()
        key, count = line.rsplit('\t', 1)
        count = int(count)
    except ValueError:
        continue

    if current_key == key:
        # Key chưa đổi (nghĩa là cả Word và Label đều giống dòng trước)
        current_count += count
    else:
        # Key đổi -> In kết quả của key trước
        if current_key:
            print(f"{current_key}\t{current_count}")
        
        # Reset
        current_key = key
        current_count = count

# In dòng cuối cùng
if current_key:
    print(f"{current_key}\t{current_count}")