# Hưỡng dẫn chạy Kmean với hadoop
- Tạo thư mục đầu vào trong hdfs
```cmd
hdfs dfs -mkdir /input/kmeans
```
- Đẩy file data-kmeans.txt vào folder k-input vừa tạo
```cmd
hdfs dfs -put ./data-kmeans.txt /input/kmeans
```
- Thêm quyền thực thi:
```cmd
chmod +x mapper.py reducer.py kmeans.sh
chmod +x /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar
```
- Chạy trực tiếp với map reduce trên hadoop chỉ 1 vòng lặp
```cmd
hadoop jar /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar \
    -files mapper.py,reducer.py,centroids.txt \
    -mapper mapper.py \
    -reducer reducer.py \
    -input /input/kmeans/data-kmeans.txt \
    -output /output/kmeans_iter_1
```
- Kết quả chạy mong đợi
```cmd
root@ed5478ed1318:~/big_data/kmean# hdfs dfs -cat /output/kmeans_iter_1/part-00000
29.6000,66.8000
43.2000,16.7000
55.1000,46.1000
```
- Chạy thuật toán đến khi tối ứu, chú ý ghi tâm khởi tạo tại file  [initial_centroids.txt](/kmean/initial_centroids.txt)
```cmd
/bin/bash kmeans.sh
```