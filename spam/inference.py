#!/usr/bin/env python3
import sys
import math
import re
from typing import Dict, Set, List

class SpamInference:
    def __init__(self) -> None:
        # Lưu trữ số lần xuất hiện của từ: {'spam': {'money': 5, ...}, 'ham': {'hi': 10, ...}}
        self.word_counts: Dict[str, Dict[str, int]] = {}
        
        # Lưu trữ số lượng văn bản của từng nhãn (từ dòng CLASS,...)
        # Dùng để tính xác suất Tiên nghiệm P(Class)
        self.doc_counts: Dict[str, int] = {}
        
        # Tổng số từ (word tokens) của từng nhãn (Tính tổng từ word_counts)
        # Dùng làm mẫu số cho P(Word|Class)
        self.total_words_per_class: Dict[str, int] = {}
        
        # Tập từ điển (Vocabulary) dùng cho Laplace Smoothing
        self.vocab: Set[str] = set()

    def clean_text(self, text: str) -> str:
        """
        Hàm này PHẢI GIỐNG HỆT logic trong mapper.py
        """
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text

    def load_model(self, file_path: str) -> None:
        """Đọc file output từ Reducer"""
        print(f"[-] Đang tải model từ {file_path}...")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line: continue
                
                try:
                    # Format reducer: Key \t Count
                    key_part, count_part = line.split('\t')
                    count = int(count_part)
                    
                    # Tách Key thành Word và Label
                    # Key format: word,label HOẶC CLASS,label
                    key_name, label = key_part.rsplit(',', 1)
                    
                    # Khởi tạo dict cho nhãn nếu chưa có
                    if label not in self.word_counts:
                        self.word_counts[label] = {}
                        self.doc_counts[label] = 0
                        self.total_words_per_class[label] = 0

                    # TRƯỜNG HỢP 1: Dòng đếm số lượng văn bản (Priors)
                    if key_name == "CLASS":
                        self.doc_counts[label] += count
                    
                    # TRƯỜNG HỢP 2: Dòng đếm từ (Likelihoods)
                    else:
                        self.word_counts[label][key_name] = count
                        self.total_words_per_class[label] += count
                        self.vocab.add(key_name)
                        
                except ValueError:
                    continue
        
        print("[-] Hoàn tất tải model.")
        print(f"[-] Số lượng Documents mỗi lớp: {self.doc_counts}")
        print(f"[-] Tổng số từ mỗi lớp: {self.total_words_per_class}")
        print(f"[-] Kích thước từ điển (V): {len(self.vocab)}")

    def predict(self, text: str) -> Dict[str, float]:
        """Tính điểm cho input text"""
        # 1. Tiền xử lý giống hệt Mapper
        clean_input = self.clean_text(text)
        words = [w for w in clean_input.split(" ") if w]
        
        scores: Dict[str, float] = {}
        
        # Tổng số văn bản trong tập train
        total_docs = sum(self.doc_counts.values())
        V = len(self.vocab) # Kích thước từ điển
        
        # Lấy danh sách các nhãn (ví dụ: spam, ham)
        # Lưu ý: lấy từ doc_counts để đảm bảo chỉ xét nhãn hợp lệ
        labels = self.doc_counts.keys()

        for label in labels:
            # --- BƯỚC 1: TÍNH PRIOR (Xác suất tiên nghiệm) ---
            # P(Class) = Số docs của class / Tổng số docs
            # Dùng log để tránh số quá nhỏ
            if total_docs > 0:
                prior = math.log(self.doc_counts[label] / total_docs)
            else:
                prior = 0.0

            # --- BƯỚC 2: TÍNH LIKELIHOOD (Xác suất có điều kiện) ---
            log_likelihood = 0.0
            
            # Mẫu số: Tổng số từ của class đó + Kích thước từ điển (Smoothing)
            denominator = self.total_words_per_class[label] + V
            
            for word in words:
                # Tử số: Số lần từ xuất hiện trong class đó + 1 (Smoothing)
                count_w = self.word_counts[label].get(word, 0)
                prob = (count_w + 1) / denominator
                log_likelihood += math.log(prob)
            
            # --- BƯỚC 3: TỔNG HỢP ---
            scores[label] = prior + log_likelihood
            
        return scores

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Tên file output từ bước MapReduce
    MODEL_FILE = "model.txt"
    
    # Khởi tạo và load model
    classifier = SpamInference()
    
    # Kiểm tra xem file có tồn tại không
    try:
        classifier.load_model(MODEL_FILE)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{MODEL_FILE}'. Hãy chạy MapReduce và lưu kết quả vào file này trước.")
        sys.exit(1)

    print("-" * 40)
    
    # Dữ liệu test
    test_inputs = [
    "Bạn được chọn nhận quà hôm nay, vui lòng xác nhận thông tin",
    "Hôm nay tôi liên hệ để gửi bạn thông tin mới nhất"
    ]

    for text in test_inputs:
        scores = classifier.predict(text)
        
        # Tìm nhãn có điểm cao nhất (Lưu ý: điểm là số âm, càng gần 0 càng lớn)
        # Sử dụng lambda để so sánh giá trị value của dict
        predicted_label = max(scores, key=lambda k: scores[k])
        
        print(f"Input: '{text}'")
        print(f"Scores: { {k: round(v, 2) for k, v in scores.items()} }")
        print(f"==> PREDICTION: {predicted_label.upper()}")
        print("-" * 40)