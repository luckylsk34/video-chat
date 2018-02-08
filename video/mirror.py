import cv2

def show_webcam(mirror=False):
	cam = cv2.VideoCapture(0)
	
	cam.set(3, 1920)
	cam.set(4, 1080)

	while True:
		ret_val, img = cam.read()
		if mirror:
			img = cv2.flip(img, 1)
		cv2.imshow('my webcam', img)
		if cv2.waitKey(1) & 0xFF == ord('q'): 
			break  # q to quit
	cv2.destroyAllWindows()

show_webcam(mirror=True)