#!/usr/bin/env python3
import sys
import math
from typing import Dict, Set

class TennisNaiveBayes:
    def __init__(self) -> None:
        # data[Label][Feature_Value] = Count
        # Ví dụ: data['Yes']['Outlook_Sunny'] = 2
        self.data: Dict[str, Dict[str, int]] = {'Yes': {}, 'No': {}}
        
        # Đếm tổng số mẫu (rows) của từng Class (P(Yes), P(No))
        self.class_counts: Dict[str, int] = {'Yes': 0, 'No': 0}
        
        # Đếm số lượng giá trị duy nhất cho mỗi đặc trưng (để làm Smoothing)
        # Ví dụ: domain_sizes['Outlook'] = 3 (Sunny, Overcast, Rain)
        self.domain_sizes: Dict[str, Set[str]] = {}

    def load_model(self, file_path: str) -> None:
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    # Line format: Key,Label \t Count
                    key_part, count_part = line.strip().split('\t')
                    count = int(count_part)
                    key_name, label = key_part.split(',') # Tách Key và Label
                    
                    # Xử lý dòng đếm tổng Class
                    if key_name == "CLASS":
                        self.class_counts[label] = count
                        continue
                    
                    # Xử lý các dòng đặc trưng (Outlook_Sunny, ...)
                    if label in self.data:
                        self.data[label][key_name] = count
                        
                        # Tự động tính domain size (V) cho từng đặc trưng
                        # Tách 'Outlook_Sunny' thành 'Outlook' và 'Sunny'
                        if '_' in key_name:
                            feature_prefix = key_name.split('_')[0]
                            if feature_prefix not in self.domain_sizes:
                                self.domain_sizes[feature_prefix] = set()
                            self.domain_sizes[feature_prefix].add(key_name)
                            
                except ValueError:
                    continue
        
        print("[-] Model Loaded.")
        print(f"[-] Class Counts: {self.class_counts}")
        print(f"[-] Domain Sizes: { {k: len(v) for k, v in self.domain_sizes.items()} }")

    def predict(self, features: Dict[str, str]) -> Dict[str, float]:
        """
        features input: {'Outlook': 'Sunny', 'Temp': 'Cool', ...}
        """
        scores: Dict[str, float] = {}
        total_samples = sum(self.class_counts.values())
        
        for label in ['Yes', 'No']:
            # 1. Tính Prior P(Class)
            # Dùng Log để tránh số quá nhỏ
            prior = math.log(self.class_counts[label] / total_samples)
            
            likelihood_sum = 0.0
            
            # 2. Tính Likelihood P(Feature|Class) cho từng đặc trưng
            for name, value in features.items():
                # Tạo key tìm kiếm, ví dụ: Outlook_Sunny
                search_key = f"{name}_{value}"
                
                # Lấy số lần xuất hiện (nếu không có thì bằng 0)
                count = self.data[label].get(search_key, 0)
                
                # Xác định V (số lượng giá trị của đặc trưng này)
                V = len(self.domain_sizes.get(name, set()))
                if V == 0: V = 1 # Tránh chia cho 0 nếu feature lạ
                
                # Công thức Smoothing cho Categorical:
                # P = (Count + 1) / (Tổng số dòng của Class + V)
                prob = (count + 1) / (self.class_counts[label] + V)
                
                likelihood_sum += math.log(prob)
            
            scores[label] = prior + likelihood_sum
            
        return scores

# --- CHẠY THỬ ---
if __name__ == "__main__":
    nb = TennisNaiveBayes()
    
    # Giả sử bạn đã chạy MapReduce và có file model.txt
    try:
        nb.load_model("model.txt")
    except FileNotFoundError:
        print("Chưa có file model.txt. Hãy chạy MapReduce trước!")
        sys.exit(0)

    print("-" * 30)
    
    # Test case: Sunny, Cool, High, Strong -> ???
    input_data = {
        "Outlook": "Sunny",
        "Temp": "Cool",
        "Humidity": "High",
        "Wind": "Strong"
    }
    
    scores = nb.predict(input_data)
    result = max(scores, key=lambda k: scores[k])
    
    print(f"Input: {input_data}")
    print(f"Scores: {scores}")
    print(f"==> Prediction: {result}")