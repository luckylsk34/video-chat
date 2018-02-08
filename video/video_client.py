import socket
import cv2
import numpy as np
from time import time

clientsocket = socket.socket()
host = '192.168.1.107'
port = 9996
clientsocket.connect((host, port))

c1 = time()
i = 0
while True:
	lv2size = (clientsocket.recv(1)).decode('ascii')
	lv1size = (clientsocket.recv(int(lv2size))).decode('ascii')
	img = clientsocket.recv(int(lv1size))


	nparr = np.fromstring(img, np.uint8)
	img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
	img = cv2.flip(img, 1)
	try:
		cv2.imshow('server', img)
	except:
		i+= 1
		continue
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break  # q to quit

c2 = time()
mi = int((c2-c1)/60)
if mi == 0:
	print('\n\nerrors: ', i, '\ntime taken: %0.1f seconds'% (c2-c1), '\n')
else:
	print('\n\nerrors: ', i, '\ntime taken: %d min %0.1f seconds'% (mi, c2-c1), '\n')