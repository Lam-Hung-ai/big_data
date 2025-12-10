#!/usr/bin/env python3
import sys
import math

def get_dist(p1, p2):
    sum_sq = sum([(a - b) ** 2 for a, b in zip(p1, p2)])
    return math.sqrt(sum_sq)

def process(input: str) -> list[float]:
    parts = input.strip().split(',')
    parts = [x.strip() for x in parts if x]
    if len(parts) == 0: return []
    try:
        point = [float(x) for x in parts]
    except ValueError:
        return []
    return point

centroids = []
try:
    with open('centroids.txt', 'r') as f:
        for line in f:
            point = process(line)
            if len(point) > 0:
                centroids.append(point)
except IOError:
    pass

for line in sys.stdin:
    
    point = process(line)
    if len(point) == 0: continue

    min_dist = float('inf')
    closest_center_index = -1
    
    for idx, center in enumerate(centroids):
        dist = get_dist(point, center)
        if dist < min_dist:
            min_dist = dist
            closest_center_index = idx
            
    print(f"{",".join(map(str, centroids[closest_center_index]))}\t{line}")