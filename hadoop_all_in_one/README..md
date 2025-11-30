## Hướng dẫn tự tạo docker images chứa toàn bộ hadoop
- Điều kiện tiên quyết phải tải [docker cho window](https://docs.docker.com/desktop/setup/install/windows-install/) hoặc [docker cho ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- Đối với hệ điều hành ubuntu thì cần thêm user chính vào nhóm docker [theo đường link](https://docs.docker.com/engine/install/linux-postinstall/)
- Tải hadoop phiên bản [3.4.2](https://dlcdn.apache.org/hadoop/common/hadoop-3.4.2/hadoop-3.4.2.tar.gz) về máy tính và lưu vào thư mục /big_data/hadoop_all_in_one
- Tại thư mục /big_data/hadoop_all_in_one, chạy lệnh trên terminal để build
```cmd
docker build -t myhadoop:3.4.2 .
```
- Khởi tạo docker với hadoop:
```cmd
docker run -it --name hadoop_all_in_one myhadoop:3.4.2
```
- Khi chạy xong có thể kiểm tra xem mọi thứ chạy ổn không
```cmd
jps
```
- Mong đợi terminal sẽ hiện ra đầy đủ:
```cmd
root@ed5478ed1318:/# jps
725 ResourceManager
1222 Jps
854 NodeManager
150 NameNode
300 DataNode
492 SecondaryNameNode
```

## Hướng dẫn dùng VS code để chỉnh sửa code trực tiếp trong docker
- Cài đặt tiện ích docker trên VS code  

![Docker extention](/images/docker_extention.png)  
- Chọn chính xác docker với hadoop để có thể vào trong docker đó chỉnh sửa file. Sau đó chọn **Attach Visual Studio Code**  

![Choose docker with hadoop in VS code](/images/choose_docker_images.png)