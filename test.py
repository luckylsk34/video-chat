import socket
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time
from threading import Thread
from queue import Queue

class serverWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #self.setFixedSize(400, 300)
        self.resize(400, 300)
        self.frame = self.frameGeometry()
        self.width = self.frame.width()
        self.height = self.height()
        self.setWindowTitle('server')
        self.setWindowIcon(QIcon('hello1.ico'))
        self.center()

        self.font = QFont()
        self.font.setFamily('yu gothic')
        self.font.setPointSize(16)
        self.font.setBold(True)

        self.lbl1 = QLabel('server started', self)
        self.lbl1.setFont(self.font)
        self.centerwidget(self.lbl1, 60)
        self.lbl2 = QLabel('host: '+socket.gethostbyname(socket.getfqdn()), self)
        self.centerwidget(self.lbl2, 150)
        self.lbl3 = QLabel('waiting for connections...', self)
        self.centerwidget(self.lbl3, 180)

        self.clientconnected = False

        self.t1 = Thread(target = self.textuntilconnection)
        self.t1.setDaemon(True)
        self.t1.start()

        self.t = Queue()
        self.t.put(self.t1)

        self.show()
        '''time.sleep(2)
        self.resize(800, 700)'''

    def center(self):
    	cp = QDesktopWidget().availableGeometry().center()
    	self.frame.moveCenter(cp)
    	self.move(self.frame.topLeft())

    def textuntilconnection(self):
        while not self.clientconnected:
            self.lbl3.setText('waiting for connections.')
            if not self.clientconnected:
                time.sleep(0.125)
            self.lbl3.setText('waiting for connections..')
            if not self.clientconnected:
                time.sleep(0.125)
            self.lbl3.setText('waiting for connections...')
            if not self.clientconnected:
                  time.sleep(0.125)

    def removetext(self):
    	time.sleep(0.125)
    	self.lbl1.deleteLater()
    	self.lbl2.deleteLater()
    	self.lbl3.deleteLater()

    def centerwidget(self, a, pos):
    	a.resize(a.sizeHint())
    	a.move((self.width-a.frameGeometry().width())/2, pos)


if __name__ == '__main__':
	app = QApplication([])
	server = serverWindow()
	sys.exit(app.exec_())
