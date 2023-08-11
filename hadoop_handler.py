import pydoop.hdfs as hdfs

class HadoopHandler:
    def __init__(self, host='localhost', port=9000):
        self.hdfs = hdfs.hdfs(host, port)

    def read(self, hdfs_path):
        with hdfs.open(hdfs_path) as f:
            data = f.read()
        return data

    def write(self, hdfs_path, data):
        with hdfs.open(hdfs_path, 'w') as f:
            f.write(data)

    def list_dir(self, hdfs_path):
        return hdfs.ls(hdfs_path)

    def exists(self, hdfs_path):
        return hdfs.path.exists(hdfs_path)

    def delete(self, hdfs_path):
        hdfs.rmr(hdfs_path)

hadoop_handler = HadoopHandler()

# Write data to HDFS
hadoop_handler.write('/user/hadoop/data.txt', 'Hello, Hadoop!')

# Read data from HDFS
data = hadoop_handler.read('/user/hadoop/data.txt')
print(data)

# List directory
files = hadoop_handler.list_dir('/user/hadoop')
print(files)

# Check if path exists
print(hadoop_handler.exists('/user/hadoop/data.txt'))

# Delete file
hadoop_handler.delete('/user/hadoop/data.txt')
