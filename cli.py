import socket

HOST = '192.168.0.29'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    recvData = s.recv(1024)
    print('상대방 :', recvData.decode('utf-8'))
    sendData = input('>>>')
    s.send(sendData.encode('utf-8'))


s.close()
