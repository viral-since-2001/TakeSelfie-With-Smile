import cv2
from random import randrange
import datetime
import time


cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    frame2 = frame.copy()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      
      
    # Applying HARCASCADE Algorithm to our Project 
    trained_frame = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #for face
    trained_smile = cv2.CascadeClassifier('haarcascade_smile.xml') # for smile
    frame_co_ordination = trained_frame.detectMultiScale(gray)

    r = 255
    g = 255
    b = 255
    for (x, y, w, h) in frame_co_ordination:
        face_slices = frame[y:y+h, x:x+w]
        gray_slices = frame[y:y+h, x:x+w]

        smile_co = trained_smile.detectMultiScale(gray_slices,1.7, 20)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,g,0), 4)
        for (x_, y_, w_, h_) in smile_co:
            cv2.rectangle(face_slices, (x_, y_), (x_+w_, y_+h_), (r,0,b) , 4)
            file_name_tag = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            file_name = f'justSmile-{file_name_tag}.png'
            cv2.imwrite(file_name, frame2)
            time.sleep(10)
        if len(smile_co) > 0: 
            Text = 'Smiling'
            cv2.putText(frame, Text, (x, y+h+40), cv2.FONT_HERSHEY_COMPLEX, 1, (r,g,b))



    cv2.imshow('my face', frame)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



