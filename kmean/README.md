# Hưỡng dẫn chạy Kmean với hadoop
- Tạo thư mục đầu vào trong hdfs
```cmd
hdfs dfs -mkdir /k-input
```
- Đẩy file data-kmeans.txt vào folder k-input vừa tạo
```cmd
hadoop fs -put ./data-kmeans.txt /k-input
```