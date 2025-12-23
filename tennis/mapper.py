#!/usr/bin/env python3
import sys

# Định nghĩa tên các cột đặc trưng (Feature) theo thứ tự
FEATURE_NAMES = ["Outlook", "Temp", "Humidity", "Wind"]

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line or line.startswith("Outlook"): # Bỏ qua header hoặc dòng trống
            continue
            
        parts = line.split(',')
        if len(parts) < 5: continue

        # Cột cuối cùng là Label (Play Tennis: Yes/No)
        label = parts[-1]
        features = parts[:-1]

        # 1. Emit tổng số dòng của từng Class (để tính Prior P(Yes), P(No))
        # Format: CLASS,Yes \t 1
        print(f"CLASS,{label}\t1")

        # 2. Emit từng đặc trưng kèm Label
        # Format: Outlook_Sunny,Yes \t 1
        for i, value in enumerate(features):
            feature_name = FEATURE_NAMES[i]
            # Tạo key kết hợp: TênCột_GiáTrị
            key = f"{feature_name}_{value}"
            print(f"{key},{label}\t1")

if __name__ == "__main__":
    main()