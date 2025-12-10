#!/bin/bash

# Khởi tạo
cp initial_centroids.txt centroids.txt
ITERS=1
MAX_ITERS=3

while [ $ITERS -lt $MAX_ITERS ]; do
    echo "Running iteration $((ITERS))"
    
    # Xóa output cũ trên HDFS nếu có
    hdfs dfs -cat /output/kmeans_out/part-00000
    hdfs dfs -rm -r /output/kmeans_out
    # Chạy Job
    hadoop jar /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar \
        -files mapper.py \
        -files reducer.py \
        -files centroids.txt \
        -mapper mapper.py \
        -reducer reducer.py \
        -input /input/kmeans/data-kmeans.txt \
        -output /output/kmeans_out
    
    # Lấy kết quả về
    hdfs dfs -getmerge /output/kmeans_out new_centroids.txt
    
    # (Ở đây bạn nên thêm code so sánh sự thay đổi giữa centroids.txt và new_centroids.txt)
    # Nếu giống nhau -> break
    
    # Cập nhật centroids cho vòng sau
    mv new_centroids.txt centroids.txt
    
    let ITERS=$((ITERS+1))
done