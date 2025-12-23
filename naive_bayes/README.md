# Hướng dẫn chạy chương trình Google Word Count với hadoop
- Tại thư mục big_data/google_word_count, thêm các file trong thư mục data vào folder /input_naive_bayes của hdfs
```cmd
hdfs dfs -mkdir /input_naive_bayes
hdfs dfs -put ./iris.csv /input_naive_bayes
```
- Thêm quyền chạy cho mapper và reducer
```cmd
chmod +x mapper_train.py reducer_train.py
```

- Thêm quyền thực thi:
```cmd
chmod +x /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar
```
- Chạy trực tiếp với map reduce trên hadoop
```cmd
hadoop jar /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar	\
-files mapper_train.py,reducer_train.py	\
-mapper mapper_train.py \
-reducer reducer_train.py	\
-input /input_naive_bayes	\
-output /train_naive_bayes	
```
- Kết quả mong đợi
```result
root@cca6f7f5b5ee:~/big_data/naive_bayes# hdfs dfs -cat /train_naive_bayes/part-00000
{"Iris-setosa": {"col:0": [5.006, 0.12176400000000002], "col:1": [3.418, 0.142276], "col:2": [1.464, 0.029504000000000002], "col:3": [0.24400000000000002, 0.011264000000000001]}}
{"Iris-versicolor": {"col:0": [5.936, 0.261104], "col:1": [2.77, 0.0965], "col:2": [4.26, 0.21640000000000004], "col:3": [1.3259999999999998, 0.038324]}}
{"Iris-virginica": {"col:0": [6.587999999999999, 0.39625600000000005], "col:1": [2.9739999999999998, 0.10192399999999999], "col:2": [5.5520000000000005, 0.29849600000000004], "col:3": [2.026, 0.07392399999999999]}}
```
- Lấy kết quả train lưu vào folder hiện tại
```cmd
hdfs dfs -getmerge /train_naive_bayes/part-00000 weight.json
```