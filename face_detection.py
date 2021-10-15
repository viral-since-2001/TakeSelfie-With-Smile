import cv2
from random import randrange
import datetime
import time

'''

frame = cv2.imread('crop.png')

gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray_img, (5,5), 0)
_, thres = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
dialated = cv2.dilate(thres, None, 3)
trained_img = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img_co_ordinate = trained_img.detectMultiScale(gray_img)
contours,_ = cv2.findContours(dialated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   

# print(img_co_ordinate)
(x,y,w,h) = img_co_ordinate[1]
# print(x,y,w,h)
for (x,y,w,h) in img_co_ordinate:
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    cv2.drawContours(contours, contours, -1, (r,g,b))
    cv2.rectangle(frame, (x,y),(x+w, y+h),(r,g,b), 4)
    print(r,b,g)


# cv2.imshow('frame', frame)
# # cv2.imshow('gray', gray_img)
# cv2.waitKey()
    '''


cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    frame2 = frame.copy()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    trained_frame = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    trained_smile = cv2.CascadeClassifier('haarcascade_smile.xml')
    frame_co_ordination = trained_frame.detectMultiScale(gray)

    # print(frame_co_ordination)
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
        # (x_, y_, w_, h_) = smile_co[0]
        if len(smile_co) > 0: 
            Text = 'Smiling'
            cv2.putText(frame, Text, (x, y+h+40), cv2.FONT_HERSHEY_COMPLEX, 1, (r,g,b))



    cv2.imshow('my face', frame)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



