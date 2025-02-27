import cv2
import numpy as np

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter('craigvideo1.mp4',cv2.VideoWriter_fourcc(*'dvc'),20,(width,height))

while True:
    ret, frame = cap.read()

    writer.write(frame)


    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()