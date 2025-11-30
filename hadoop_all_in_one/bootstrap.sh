#!/bin/bash

# Khởi động SSH service
service ssh start

# Format NameNode nếu chưa được format (chỉ làm lần đầu)
if [ ! -d "/tmp/hadoop-root/dfs/name" ]; then
    echo "Formatting NameNode..."
    $HADOOP_HOME/bin/hdfs namenode -format
fi

# Khởi động Hadoop (HDFS + YARN)
echo "Starting Hadoop services..."
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

exec /bin/bash