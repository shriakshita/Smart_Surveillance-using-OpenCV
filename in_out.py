'''import cv2
import numpy as np

cap=cv2.VideoCapture(0)

left,center,right= False,False,False
x=300

while True:
	_,frame1=cap.read()
	_,frame2=cap.read()

	g1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
	g2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

	diff=cv2.absdiff(g1,g2)
	_,thresh =cv2.threshold(diff,30,255,cv2.THRESH_BINARY)

	contr,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	if len(contr)>0:
		contr = max(contr,key=cv2.contourArea)
		x,y,w,h=cv2.boundingRect(contr)
		cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)

	#if frame is empty or not
	if not(left) and not(right):
		if x<100:
			left=True 
		elif x>500:
			right=True 

	elif left:
		if x>100 and x<500 and not(center):
			center=True

		if x>500:
			if center:
				print("motion towards right")
				center=False
				left=False
			else:
				right=True

	elif right:
		if x>100 and x<500 and not(center):
			center=True

		if x<100:
			if center:
				print("motion towards left")
				center=False
				right=False
			else:
				left=True




	cv2.imshow("Frame1",frame1)
	cv2.imshow("Frame2",thresh)

	_,frame1=cap.read()

	key=cv2.waitKey(1)

	if key == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()

import cv2
from datetime import datetime
cap = cv2.VideoCapture(0)
def in_out():
    


    right, left = "", ""

    while True:
        _, frame1 = cap.read()
        frame1 = cv2.flip(frame1, 1)
        _, frame2 = cap.read()
        frame2 = cv2.flip(frame2, 1)

        diff = cv2.absdiff(frame2, frame1)
        
        diff = cv2.blur(diff,(5,5))
        
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        
        _, threshd = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
        
        contr, _ = cv2.findContours(threshd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        x = 300
        if len(contr) > 0:
            max_cnt = max(contr, key=cv2.contourArea)
            x,y,w,h = cv2.boundingRect(max_cnt)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame1, "MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)
            
        
        if right == "" and left == "":
            if x > 500:
                right = True
            
            elif x < 200:
                left = True
                
        elif right:
                if x < 200:
                    print("to left")
                    x = 300
                    right, left = "", ""
                    cv2.imwrite(f"C:\\Users\\AKSHAY AKSHITA\\OneDrive\\Desktop\\mini project pratice(tkinter)\\visitors\\in{datetime.now().strftime('%-y-%-m-%-d-%H:%M:%S')}.jpg", frame1)
            
        elif left:
                if x > 500:
                    print("to right")
                    x = 300
                    right, left = "", ""
                    cv2.imwrite(f"C:\\Users\\AKSHAY AKSHITA\\OneDrive\\Desktop\\mini project pratice(tkinter)\\visitors\\out{datetime.now().strftime('%-y-%-m-%-d-%H:%M:%S')}.jpg", frame1)
            
            
        
        cv2.imshow("", frame1)
        
        key = cv2.waitKey(1)
        
        if key == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
'''