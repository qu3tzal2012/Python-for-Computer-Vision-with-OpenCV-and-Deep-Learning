#interactive draw on video

import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#### CALLBACK FUNCTION ####

def draw_rectangle(event,x,y,flags,param):
    
    global pt1,pt2,topLeft_clicked,botRight_clicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        #RESET the rectangle (erase previous drawn rectangle)
        if topLeft_clicked == True and botRight_clicked == True:
            pt1 = (0,0) #top left
            pt2 = (0,0) #bottom right
            topLeft_clicked = False
            botRight_clicked = False
            
        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked = True
        
        elif botRight_clicked == False:
            pt2 = (x,y)
            botRight_clicked = True

# GLOBAL VARIABLES

pt1 = (0,0) #top left
pt2 = (0,0) #bottom right
topLeft_clicked = False
botRight_clicked = False
            
#CONNECT TO CALLBACK
cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rectangle)


while True:
    ret,frame = cap.read()

    #### DRAWING ON FRAME BASED OFF GLOBAL VARIABLES
    
    if topLeft_clicked: #if top left is clicked
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)
    if topLeft_clicked and botRight_clicked: #if both are clicked
        cv2.rectangle(frame,pt1,pt2,(0,0,255),3)
    
    cv2.imshow('Test',frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()