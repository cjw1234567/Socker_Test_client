import sys,socket
from PyQt5.QtWidgets import *
from PyQt5 import uic

HOST = '192.168.0.29'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

form_class = uic.loadUiType("ux.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button1Function)



    def button1Function(self):
        print("btn_1 Clicked")
        sendData = 'a'
        s.send(sendData.encode('utf-8'))
        recvData = s.recv(1024)
        self.label.setText(str(recvData))



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
