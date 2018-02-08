from socket import *
from threading import Thread
from time import sleep
n = 0

def printserverstart():
	global n
	while not n:
		print('server listenining .  ', end = '\r')
		if not n:
			sleep(0.125)
		print('server listenining .. ', end = '\r')
		if not n:
			sleep(0.125)
		print('server listenining ...', end = '\r')
		if not n:
			sleep(0.125)

def start_server(port):
	global n
	n = 0
	server = socket()
	host = gethostname()
	server.bind((host, port))
	server.listen(5)
	Thread(target = printserverstart).start()
	client, addr = server.accept()
	n = 1

	sleep(0.225)
	print('connected to %s             ' % client)
	return server, client, addr
