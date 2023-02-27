import os
img_rows,img_cols=200,200 

listing = os.listdir(r'C:\\Users\\AKSHAY AKSHITA\\OneDrive\\Desktop\\mini project pratice(tkinter)\\recordings')

# Create a counter
counter = 0

for vid in listing:

    vid = r"C:\\Users\\AKSHAY AKSHITA\\OneDrive\\Desktop\\mini project pratice(tkinter)\\recordings"+vid
    cap = cv2.VideoCapture(vid)

    for k in range(1):

        ret, frame = cap.read()
        frame=cv2.resize(frame,(img_rows,img_cols))
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        plt.imshow(rgb)
        plt.xticks([]), plt.yticks([])  
        plt.show()

        # Create a file name 
        currentFileName = "snapshot" + str(counter) + ".jpg"

        # Save the image
        cv2.imwrite(currentFileName, rgb)

        # Increment the counter 
        counter = counter + 1 

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()