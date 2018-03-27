from pyhdfs import HdfsClient

client = HdfsClient(hosts='hadoop1:50070')

print(client.listdir('/user/hive/warehouse/repdata1'))