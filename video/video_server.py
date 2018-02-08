import cv2
from server import *

def size_(a):
	#if type(a) == type('str'):
	return len(a)

serversocket = socket()
clientsocket, addr = start_server(serversocket, 9996)
cam = cv2.VideoCapture(0)
cam.set(3, 1920)
cam.set(4, 1080)

s = 1/60

while True:
	ret, img = cam.read()
	ret, jpeg = cv2.imencode('.jpg', img)
	bts = jpeg.tobytes()
	lv1size = str(size_(bts))
	lv2size = str(size_(lv1size))
	
	clientsocket.send(lv2size.encode('ascii'))
	clientsocket.send(lv1size.encode('ascii'))
	clientsocket.send(bts)
	sleep(s)