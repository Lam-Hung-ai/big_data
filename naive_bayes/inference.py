#!/usr/bin/env python3
import json
import math

def predict(arr: list[float], cates: dict, groud_true) -> None:
    count_all = sum(cates[label]['count'] for label in cates.keys())
    prop = {} 
    for label in cates.keys():
        score = math.log(cates[label]['count']*1.0/count_all)
        sum_val = 0
        for col, value_arr in cates[label].items():
            if col == "count":
                continue
            idx = int(col.rsplit(":")[-1])
            sum_val += math.log(value_arr[1]) + (((arr[idx] - value_arr[0])**2)/value_arr[1])
        score += (-0.5)*sum_val
        prop[label] = score
    
    l = float('-inf')
    label_predict = ""
    for label, value in prop.items():
        if value > l:
            l = value
            label_predict = label
    
    print(f"Dãy dự đoán: {arr} Thực tế: {groud_true:<15} | Dự đoán: {label_predict:<15} | {'Chính xác' if label_predict == groud_true else 'Sai'}")
        
with open("weight.json") as file:
    lines = file.readlines()   

categories = {}
for line in lines:
    categories.update(json.loads(line.strip()))

with open("iris.csv") as file:
    for line in file.readlines():
        line = line.strip()
        if not line:
            continue
        elements = line.split(",")
        if len(elements) != 5:
            continue
        
        value = []
        try:
            for i in range(len(elements) -1):
                value.append(float(elements[i]))
            predict(value, categories, elements[-1])
        except ValueError:
            continue        
with open("weight.json") as file:
    lines = file.readlines()   

categories = {}
for line in lines:
    categories.update(json.loads(line.strip()))

with open("iris.csv") as file:
    for line in file.readlines():
        line = line.strip()
        if not line:
            continue
        elements = line.split(",")
        if len(elements) != 5:
            continue
        
        value = []
        try:
            for i in range(len(elements) -1):
                value.append(float(elements[i]))
            predict(value, categories, elements[-1])
        except ValueError:
            continue