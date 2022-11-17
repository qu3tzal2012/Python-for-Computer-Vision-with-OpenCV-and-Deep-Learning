import cv2
import time

cap = cv2.VideoCapture('cup.mp4')

if cap.isOpened() == False:
    print('ERROR!  FILE NOT FOUND OR WRONG CODEC')

while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:

        # WRITER AT 20 FPS
        time.sleep(1/5) # displays frames at rate they were recording
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    else:
        break