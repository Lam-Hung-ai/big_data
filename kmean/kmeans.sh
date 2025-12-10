#!/bin/bash

# --- CẤU HÌNH ---
HADOOP_JAR="/opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar"
INPUT_PATH="/input/kmeans/data-kmeans.txt"
OUTPUT_PATH="/output/kmeans_out"
LOCAL_CENTROIDS="centroids.txt"
NEW_CENTROIDS="new_centroids.txt"
INITIAL_CENTROIDS="initial_centroids.txt"

MAX_ITERS=10 
CTR=1         

if [ ! -f $INITIAL_CENTROIDS ]; then
    echo "Lỗi: Không tìm thấy file $INITIAL_CENTROIDS"
    exit 1
fi
cp $INITIAL_CENTROIDS $LOCAL_CENTROIDS

echo "------------ BẮT ĐẦU TRAINING K-MEANS ------------"

# 2. Vòng lặp chính
while [ $CTR -le $MAX_ITERS ]; do
    echo "=================================================="
    echo "VÒNG LẶP THỨ: $CTR/$MAX_ITERS"
    echo "=================================================="

    hdfs dfs -rm -r $OUTPUT_PATH &> /dev/null

    hadoop jar $HADOOP_JAR \
        -file mapper.py \
        -file reducer.py \
        -file $LOCAL_CENTROIDS \
        -mapper mapper.py \
        -reducer reducer.py \
        -input $INPUT_PATH \
        -output $OUTPUT_PATH

    if [ $? -ne 0 ]; then
        echo "Lỗi: Hadoop Job bị fail ở vòng lặp $CTR!"
        exit 1
    fi

    rm -f $NEW_CENTROIDS
    hdfs dfs -getmerge $OUTPUT_PATH $NEW_CENTROIDS

    if [ ! -s $NEW_CENTROIDS ]; then
        echo "Lỗi: File kết quả rỗng! Kiểm tra lại Mapper/Reducer."
        exit 1
    fi

    sort $LOCAL_CENTROIDS > sorted_old.txt
    sort $NEW_CENTROIDS > sorted_new.txt

    diff -q sorted_old.txt sorted_new.txt > /dev/null
    
    if [ $? -eq 0 ]; then
        echo ">>> THÀNH CÔNG: Thuật toán đã hội tụ sau $CTR vòng lặp!"
        echo ">>> Tâm cuối cùng nằm trong file: $LOCAL_CENTROIDS"
        break
    else
        echo ">>> Chưa hội tụ. Cập nhật tâm mới và tiếp tục..."
        mv $NEW_CENTROIDS $LOCAL_CENTROIDS
    fi
    CTR=$((CTR+1))
done

rm -f sorted_old.txt sorted_new.txt

if [ $CTR -eq $MAX_ITERS ]; then
    echo ">>> CẢNH BÁO: Đã chạy hết $MAX_ITERS vòng lặp mà chưa hội tụ hoàn toàn."
fi