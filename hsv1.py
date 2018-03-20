import cv2
import numpy as np
cap=cv2.VideoCapture(0)
lh=[0,100,100]
uh=[0,0,0]

while(1):
	_,img=cap.read()
	cv2.circle(img,(325,215),90,(0,255,0),3)
	font=cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img,'Press "c" to get color values',(20,20),font,0.5,(255,0,0),1,cv2.CV_AA)
	cv2.putText(img,'Press "q" to exit',(20,40),font,0.5,(255,0,0),1,cv2.CV_AA)
#	cv2.imshow("Color spaces from cam",img)
	k=cv2.waitKey(5) & 0xFF
	if(k==ord('c')):
		j=img[177:256,277:366]
		l=np.average(j,axis=0)
		m=np.average(l,axis=0)
		bgr=np.uint8([[m]])
		hsv=cv2.cvtColor(bgr,cv2.COLOR_BGR2HSV)
		b=hsv[0]
		c=b[0]

		lh[0]=c[0]-10
		uh[0]=c[0]+10
		uh[1]=c[1]
		uh[2]=c[2]

		print("Color spaces")
		print("hsv ",lh," ",uh)
		print()
	if (k == ord('q')):
		break
cap.release()
cv2.destroyAllWindows()
