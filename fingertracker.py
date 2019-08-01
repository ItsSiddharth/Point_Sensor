import cv2
import time

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #frame = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
    mask = cv2.inRange(frame, (0,100,100),(20,255,225))
    mask = cv2.flip( mask, 1 )
    im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours( mask, contours, 3, (0,255,0), 3)
    cnt = contours[0]
    topmost = tuple(cnt[cnt[:,:,1].argmin()][0])

    
    


    cv2.imshow('mask', mask)
    cv2.imshow('img', frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print(topmost)
    time.sleep(0.1)
    

cap.release()
cv2.destroyAllWindows()