# Hướng dẫn chạy chương trình Word Count với hadoop
- Tại thư mục big_data/word_count, thêm data.txt vào folder input của hdfs
``cmd
hdfs dfs -mkdir /input
hdfs dfs -put ./data.txt /input
```
- Thêm quyền chạy cho mapper.py và reducer.py
```cmd
chmod +x mapper.py reducer.py
```
- Test chạy thử
```cmd
cat data.txt | ./mapper.py | sort | ./reducer.py
```
Mong đợi kết quả
```result
BUS     2
Bus     1
CAR     1
Car     1
TRAIN   2
buS     1
bus     3
caR     1
car     4
train   2
```
- Thêm quyền thực thi:
```cmd
chmod +x /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar
```
- Chạy trực tiếp với map reduce trên hadoop
```cmd
hadoop jar /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar \
    -input /input/data.txt \
    -output /output/wordcount \
    -mapper mapper.py \
    -reducer reducer.py \
    -file mapper.py \
    -file reducer.py
```
- Kết quả mong đợi
```result
hdfs dfs -cat /output/wordcount/part-00000
BUS     2
Bus     1
CAR     1
Car     1
TRAIN   2
buS     1
bus     3
caR     1
car     4
train   2
```
