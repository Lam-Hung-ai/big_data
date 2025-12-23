#!/usr/bin/env python3
import sys
import re

def clean_text(text):
    # Chuyển về chữ thường và loại bỏ dấu câu cơ bản
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

for line in sys.stdin:
    line = line.strip()
    if not line: continue
    text, label = line.rsplit(",", 1)
    text = clean_text(text)
    print(f"CLASS,{label}\t1")
    text = [word for word in text.split(" ") if word]
    for word in text:
        print(f"{word},{label}\t1")
