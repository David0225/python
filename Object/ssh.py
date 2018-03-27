import paramiko

ssh = paramiko.SSHClient()

ssh.connect(hostname='10.99.68.249',port=22,username='root',password='123456')