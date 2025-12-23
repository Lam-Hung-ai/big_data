# Hướng dẫn chạy chương trình Word Count với hadoop
- Tại thư mục big_data /tennis, thêm train.txt vào folder input của hdfs
```cmd
hdfs dfs -mkdir /tennis
hdfs dfs -put train.txt /tennis
```
- Thêm quyền chạy cho mapper.py và reducer.py
```cmd
chmod +x mapper.py reducer.py inference.py
```
- Test chạy thử
```cmd
cat train.txt | ./mapper.py | sort | ./reducer.py
```
Mong đợi kết quả
```result
CLASS,No        5
CLASS,Yes       9
Humidity_High,No        4
Humidity_High,Yes       3
Humidity_Normal,No      1
Humidity_Normal,Yes     6
Outlook_Overcast,Yes    4
Outlook_Rain,No 2
Outlook_Rain,Yes        3
Outlook_Sunny,No        3
Outlook_Sunny,Yes       2
Temp_Cool,No    1
Temp_Cool,Yes   3
Temp_Hot,No     2
Temp_Hot,Yes    2
Temp_Mild,No    2
Temp_Mild,Yes   4
Wind_Strong,No  3
Wind_Strong,Yes 3
Wind_Weak,No    2
Wind_Weak,Yes   6
```
- Thêm quyền thực thi:
```cmd
chmod +x /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar
```
- Chạy trực tiếp với map reduce trên hadoop
```cmd
hadoop jar /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar \
    -input /tennis/train.txt \
    -output /output/tennis \
    -file mapper.py \
    -file reducer.py \
    -mapper mapper.py \
    -reducer reducer.py 
```
- Kết quả mong đợi
```result
root@cca6f7f5b5ee:~/big_data/tennis# hdfs dfs -cat /output/tennis/part-00000
CLASS,No        5
CLASS,Yes       9
Humidity_High,No        4
Humidity_High,Yes       3
Humidity_Normal,No      1
Humidity_Normal,Yes     6
Outlook_Overcast,Yes    4
Outlook_Rain,No 2
Outlook_Rain,Yes        3
Outlook_Sunny,No        3
Outlook_Sunny,Yes       2
Temp_Cool,No    1
Temp_Cool,Yes   3
Temp_Hot,No     2
Temp_Hot,Yes    2
Temp_Mild,No    2
Temp_Mild,Yes   4
Wind_Strong,No  3
Wind_Strong,Yes 3
Wind_Weak,No    2
Wind_Weak,Yes   6
```
- Lấy dữ liệu từ HDFS về máy local:
```cmd
hdfs dfs -cat /output/tennis/part-00000 > model.txt   
```
- Chạy inference:
```cmd
./inference.py
```
