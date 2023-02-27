import cv2
from datetime import datetime
cap = cv2.VideoCapture(0)
def in_out():
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
