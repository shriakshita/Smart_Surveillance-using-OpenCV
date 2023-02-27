import cv2	
from datetime import datetime

#def record():
cap=cv2.VideoCapture(0)

	width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

	writer=cv2.VideoWriter("C:\\Users\\AKSHAY AKSHITA\\OneDrive\\Desktop\\mini project pratice(tkinter)\\recordings\\1stvideo.mp4",cv2.VideoWriter_fourcc(*'DIVX'),20,(width,height))

	while True:
		ret,frame=cap.read()
		writer.write(frame)
		cv2.putText(frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50,50), cv2.FONT_HERSHEY_COMPLEX,
                        0.6, (255,255,255), 2)
		writer.write(frame)


		cv2.imshow('frame',frame)

		if cv2.waitKey(1) == ord("q"):
			break

	cap.release()
	writer.release()
	cv2.destroyAllWindows()