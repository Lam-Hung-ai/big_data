# Hướng dẫn chạy chương trình Word Count với hadoop
- Tại thư mục big_data /spam, thêm train.txt vào folder input của hdfs
```cmd
hdfs dfs -mkdir /spam
hdfs dfs -put train.txt /spam
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
CLASS,0 10
CLASS,1 10
bạn,0   10
bạn,1   10
bằng,1  1
cho,1   4
chào,0  1
chúc,1  1
chỉ,1   2
chọn,1  1
cuộc,0  2
cách,1  1
có,0    1
cần,0   2
cần,1   1
của,0   1
dành,1  1
dự,0    1
gửi,0   5
hoàn,1  1
hãy,0   2
hãy,1   1
hôm,0   7
hôm,1   8
hẹn,0   1
hệ,0    7
họp,0   1
hợp,0   1
khi,0   1
liên,0  7
làm,0   1
lòng,0  1
lòng,1  2
lại,0   2
lịch,0  1
miễn,1  9
mắc,0   1
mới,0   1
mừng,1  1
nay,0   7
nay,1   8
ngay,1  4
nhân,0  1
nhất,0  1
nhận,0  6
nhận,1  17
nếu,0   2
phí,1   9
quà,1   5
riêng,1 1
sự,0    1
thanh,0 1
thông,0 10
thông,1 6
thưởng,1        1
thắc,0  1
tin,0   10
tin,1   6
tiền,1  1
toàn,1  1
toán,0  1
trong,1 1
trúng,1 1
trước,0 1
tôi,0   8
việc,0  1
voucher,1       1
vui,0   1
vui,1   2
và,1    1
với,0   1
xác,0   6
xác,1   7
án,0    1
đã,1    2
đãi,1   3
được,1  3
để,0    5
để,1    1
đồng,0  1
ưu,1    3
```
- Thêm quyền thực thi:
```cmd
chmod +x /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar
```
- Chạy trực tiếp với map reduce trên hadoop
```cmd
hadoop jar /opt/hadoop-3.4.2/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar \
    -input /spam/train.txt \
    -output /output/spam \
    -file mapper.py \
    -file reducer.py \
    -mapper mapper.py \
    -reducer reducer.py 
```
- Kết quả mong đợi
```result
root@cca6f7f5b5ee:~/big_data/spam# hdfs dfs -cat /output/spam/part-00000
CLASS,0 10
CLASS,1 10
bạn,0   10
bạn,1   10
bằng,1  1
cho,1   4
chào,0  1
chúc,1  1
chỉ,1   2
chọn,1  1
cuộc,0  2
cách,1  1
có,0    1
cần,0   2
cần,1   1
của,0   1
dành,1  1
dự,0    1
gửi,0   5
hoàn,1  1
hãy,0   2
hãy,1   1
hôm,0   7
hôm,1   8
hẹn,0   1
hệ,0    7
họp,0   1
hợp,0   1
khi,0   1
liên,0  7
làm,0   1
lòng,0  1
lòng,1  2
lại,0   2
lịch,0  1
miễn,1  9
mắc,0   1
mới,0   1
mừng,1  1
nay,0   7
nay,1   8
ngay,1  4
nhân,0  1
nhất,0  1
nhận,0  6
nhận,1  17
nếu,0   2
phí,1   9
quà,1   5
riêng,1 1
sự,0    1
thanh,0 1
thông,0 10
thông,1 6
thưởng,1        1
thắc,0  1
tin,0   10
tin,1   6
tiền,1  1
toàn,1  1
toán,0  1
trong,1 1
trúng,1 1
trước,0 1
tôi,0   8
việc,0  1
voucher,1       1
vui,0   1
vui,1   2
và,1    1
với,0   1
xác,0   6
xác,1   7
án,0    1
đã,1    2
đãi,1   3
được,1  3
để,0    5
để,1    1
đồng,0  1
ưu,1    3
```
- Lấy dữ liệu từ HDFS về máy local:
```cmd
hdfs dfs -cat /output/spam/part-00000 > model.txt   
```
- Chạy inference:
```cmd
./inference.py
```
