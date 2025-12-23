#!/usr/bin/env python3
import json
import sys

def cal_avg_variance(ds: list[float]) -> tuple[float, float]:
    arg = sum(ds)*1.0/len(ds)
    var = sum((arg-element)**2 for element in ds)*1.0/len(ds)

    return (arg, var)

curren_label = ""
col_value = {}
count = 0

for line in sys.stdin:
    line = line.strip()
    elements = line.split("\t", 1)
    try:
        value = float(elements[1])   # type: ignore
    except:
        continue

    label, col= elements[0].rsplit("_", 1)
    # print(col, label)

    if curren_label== "":
        curren_label=label

    # Khác nhãn
    if label != curren_label:
        # In ra
        tmp = {key: cal_avg_variance(value_arr) for key, value_arr in col_value.items()}
        tmp["count"] = count
        print(json.dumps({curren_label: tmp}))
        # Cập nhật lại
        curren_label = label
        count = 0
        col_value = {}
        if col_value.get(col, None) is None:
            col_value[col] = [value]
        else:
            col_value[col].append(value)
    # Cùng nhãn
    else:
        if col_value.get(col, None) is None:
            col_value[col] = [value]
        else:
            col_value[col].append(value)

        count +=1

# Vì là nhãn cuối thì phải in ra
if col_value:
    tmp = {key: cal_avg_variance(value_arr) for key, value_arr in col_value.items()}
    tmp["count"] = count
    print(json.dumps({curren_label: tmp}))
 