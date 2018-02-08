from socket import *
from threading import Thread
from time import *
n = 0

def printserverstart():
	global n
	while not n:
		print('server listenining .  ', end = '\r')
		sleep(0.075)
		print('server listenining .. ', end = '\r')
		sleep(0.075)
		print('server listenining ...', end = '\r')
		sleep(0.075)

def start_server(serversocket, port):
	global n
	n = 0
	host = gethostname()
	serversocket.bind((host, port))
	serversocket.listen(5)
	Thread(target = printserverstart).start()
	tu = serversocket.accept()
	n = 1
	sleep(0.225)
	print('connected to %s             ' % tu[0])
	return tu