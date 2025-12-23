#!/usr/bin/env python3
import sys

def process(input: str) -> list[float]:
    input = input.split('\t')[0]
    parts = input.strip().split(',')
    parts = [x.strip() for x in parts if x]
    if len(parts) == 0: return []
    try:
        point = [float(x) for x in parts]
    except ValueError:
        return []
    return point

def get_point_str(point: list[float]) -> str:
    return ",".join([f"{x:.4f}" for x in point])

current_centroid = None
cluster_points = []
point_sum = []
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line: continue
    
    try:
        centroid_idx, point_str = line.split('\t')
        point = process(point_str)
    except ValueError:
        continue

    if current_centroid == centroid_idx:
        point_sum = [sum(x) for x in zip(point_sum, point)]
        count += 1
        cluster_points.append(point)
    else:
        if current_centroid is not None:
            new_center = [x / count for x in point_sum]
            all_points = [get_point_str(new_center)] + [get_point_str(p) for p in cluster_points]
            print(get_point_str(new_center)+"\t" + "\t".join(all_points))
            cluster_points = []
        
        current_centroid = centroid_idx
        point_sum = point
        count = 1

# In tâm cuối cùng
if current_centroid is not None:
    new_center = [x / count for x in point_sum]
    all_points = [get_point_str(new_center)] + [get_point_str(p) for p in cluster_points]
    print(get_point_str(new_center)+"\t" + "\t".join(all_points))