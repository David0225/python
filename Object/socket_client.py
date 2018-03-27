import socket

client = socket.socket()

client.connect(('localhost',9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd)==0:continue
    client.send(cmd.encode('utf-8'))
    cmd_res_size = client.recv(1024)
    print('接受结果大小：',cmd_res_size)
    receive_data = b''
    receive_size = 0
    while receive_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        receive_size += len(data)
        print(data.decode())
        print(receive_size)
    else:
        print('done...')


client.close()