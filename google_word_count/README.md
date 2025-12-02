# Hướng dẫn chạy chương trình Google Word Count với hadoop
- Tại thư mục big_data/google_word_count, thêm các file trong thư mục data vào folder /input_google_word_count của hdfs
```cmd
hdfs dfs -mkdir /input_google_word_count
hdfs dfs -put ./data/* /input_google_word_count
```
- Thêm quyền chạy cho mapper.py và reducer.py
```cmd
chmod +x mapper.py reducer.py
```

- Thêm quyền thực thi:
```cmd
chmod +x /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar
```
- Chạy trực tiếp với map reduce trên hadoop
```cmd
hadoop jar /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar \
    -file ./mapper.py    -mapper mapper.py \
    -file ./reducer.py   -reducer reducer.py \
    -input /input_google_word_count          -output /output_google_word_count
```
- Kết quả mong đợi
```result
root@ed5478ed1318:~/big_data/google_word_count# hdfs dfs -cat /output_google_word_count/part-00000
Dream   2       P1.txt,P3.txt
Dreams  1       P2.txt
In      3       P1.txt,P3.txt
Light   2       P1.txt,P2.txt
My      1       P2.txt
Peace   1       P2.txt
Soar    1       P3.txt
Stars   1       P1.txt
The     1       P3.txt
Through 1       P2.txt
Whispers        2       P2.txt,P3.txt
and     1       P3.txt
call    1       P1.txt
dark    2       P1.txt
dream   6       P1.txt,P2.txt,P3.txt
dreams  3       P1.txt,P2.txt,P3.txt
find    1       P2.txt
glows   2       P3.txt
guides  1       P2.txt
hearts  2       P2.txt
hope    1       P2.txt
in      3       P1.txt,P2.txt
joy     1       P3.txt
light   1       P2.txt
linger  1       P2.txt
love    1       P3.txt
me      1       P1.txt
night   3       P1.txt,P2.txt,P3.txt
of      5       P1.txt,P2.txt,P3.txt
peace   2       P2.txt
shine   2       P1.txt
silence 2       P2.txt
soar    2       P2.txt,P3.txt
stars   2       P1.txt,P3.txt
that    5       P1.txt,P2.txt
the     9       P1.txt,P2.txt,P3.txt
through 1       P2.txt
way     2       P2.txt
whisperes       1       P3.txt
whispers        4       P1.txt,P2.txt,P3.txt
with    3       P3.txt
world   2       P3.txt
```
