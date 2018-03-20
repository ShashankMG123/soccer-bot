import cv2
cap=cv2.VideoCapture(0)
k=cv2.waitKey(5) & 0xFF
while(1):
	if(k==ord('c')):
		ret,img=cap.read()
		cv2.imshow('frame',img)
		cv2.waitKey(0)
		break
	else:
		cap.release()
		cv2.destroyAllWindows()
