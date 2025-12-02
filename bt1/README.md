# Hướng dẫn chạy chương trình Word Count với hadoop
- Tại thư mục big_data/word_count, thêm data.txt vào folder input của hdfs
```cmd
hdfs dfs -mkdir /input
hdfs dfs -put ./data_bt1.txt /input
```
- Thêm quyền chạy cho mapper.py và reducer.py
```cmd
chmod +x mapper.py reducer.py
```
- Test chạy thử
```cmd
cat data_bt1.txt | ./mapper.py | sort | ./reducer.py
```
Mong đợi kết quả
```result
2022_ENG        2905.0
2022_IT 3500.0
2022_MED        3177.5
2023_ENG        3065.0
2023_IT 3700.0
2023_MED        3357.5
--------------------
HIGHEST: 2023_IT with Average: 3700.0
```
- Thêm quyền thực thi:
```cmd
chmod +x /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar
```
- Chạy trực tiếp với map reduce trên hadoop
```cmd
hadoop jar /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar \
    -input /input/data_bt1.txt \
    -output /output/bt1  \
    -mapper mapper.py \
    -reducer reducer.py \
    -file mapper.py \
    -file reducer.py
```
- Kết quả mong đợi
```result
root@ed5478ed1318:~/big_data/bt1# hdfs dfs -cat /output/bt1/part-00000
2022_ENG        2905.0
2022_IT 3500.0
2022_MED        3177.5
2023_ENG        3065.0
2023_IT 3700.0
2023_MED        3357.5
--------------------
HIGHEST: 2023_IT with Average: 3700.0
```
