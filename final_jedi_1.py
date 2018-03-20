from collections import deque
import wiringpi as wp
import numpy as np
import argparse
import imutils
import cv2
import serial
import time

wp.wiringPiSetupGpio()


def Motor(x,y,pwm):
        wp.pinMode(x,1)
        wp.pinMode(y,1)
        wp.pinMode(pwm,1)
        wp.softPwmCreate(pwm,0,100)
        return x,y,pwm
def forward(motor,speed):
        (x,y,pwm)=motor
        wp.digitalWrite(x,1)
        wp.digitalWrite(y,0)
        wp.softPwmWrite(pwm,speed)
def backward(motor,speed):
        (x,y,pwm)=motor
        wp.digitalWrite(x,0)
        wp.digitalWrite(y,1)
        wp.softPwmWrite(pwm,speed)

motor1= Motor(24,23,25) #connect motor 1 to pin 23,24
motor2= Motor(27,17,22) #connet motor 2 to pin 20 ,



ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,help="max buffer size")
args = vars(ap.parse_args())
greenUpper = (31, 255, 255)
greenLower = (0, 130, 89)
#greenLower = (8,100,100)
#greenUpper = (28,255, 255)

pts = deque(maxlen=args["buffer"])

if not args.get("video", False):
        camera = cv2.VideoCapture(0)
        camera.set(3,320)
        camera.set(4,240)
        time.sleep(0.01)
else:
        camera = cv2.VideoCapture(args["video"])

while True:
        (grabbed, frame) = camera.read()
        if args.get("video") and not grabbed:
                break
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, greenLower, greenUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        if len(cnts) > 0:
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                if radius > 10:
                        cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        a=int(x)
                        b=450-int(y)
                        r=int(radius)
                        print "x=",a, "y=",b, "z=",r,"yellow"
                        if(a>120 and a<140):
                                forward(motor1,30)
                                forward(motor2,28)
                        elif(a<120):
                                forward(motor1,27)
                                backward(motor2,25)
                        elif(a>140):
                                backward(motor1,27)
                                forward(motor2,25)
                if radius > 60:
                        greenLower2 = (140, 114, 93)
                        greenUpper2 = (179, 255, 255)

			ap = argparse.ArgumentParser()
			ap.add_argument("-v", "--video",help="path to the (optional) video file")
			ap.add_argument("-b", "--buffer", type=int, default=64,help="max buffer size")
			args = vars(ap.parse_args())
			pts = deque(maxlen=args["buffer"])

			while True:
			        (grabbed, frame) = camera.read()
			        if args.get("video") and not grabbed:
			                break
			        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

			        mask = cv2.inRange(hsv, greenLower2, greenUpper2)
			        mask = cv2.erode(mask, None, iterations=2)
			        mask = cv2.dilate(mask, None, iterations=2)

	        		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		                cv2.CHAIN_APPROX_SIMPLE)[-2]
			        center = None

			        if len(cnts) > 0:
			                c = max(cnts, key=cv2.contourArea)
			                ((x, y), radius) = cv2.minEnclosingCircle(c)
			                M = cv2.moments(c)
			                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

	                		if radius > 10:
						c = max(cnts, key=cv2.contourArea)
                                       		((x, y), radius) = cv2.minEnclosingCircle(c)

			                        cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
			                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
			                        a=int(x)
			                        b=450-int(y)
			                        r=int(radius)
		                        	print "x=",a, "y=",b, "z=",r,"green "
			                        if(a>120 and a<140):
			                                forward(motor1,30)
		                                	forward(motor2,28)
			                        elif(a<120):
			                                forward(motor1,27)
			                    		backward(motor2,25)
			                        elif(a>140):
		                                	backward(motor1,27)
			                                forward(motor2,25)
        			        if radius > 60:
                	                        c = max(cnts, key=cv2.contourArea)
	                                        ((x, y), radius) = cv2.minEnclosingCircle(c)

						cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
		                	        cv2.circle(frame, center, 5, (0, 0, 255), -1)
		                        	a=int(x)
			                        b=450-int(y)
			                        r=int(radius)
			                        print "x=",a, "y=",b, "z=",r,"green"
		        	                forward(motor1,0)
		        	                forward(motor2,0)
				else:
					forward(motor1,25)
					forward(motor2,22)
	else:
		forward(motor1,25)
		forward(motor2,22)
#        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
                break
camera.release()
cv2.destroyAllWindows()
