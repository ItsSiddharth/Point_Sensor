import cv2
import time

cap = cv2.VideoCapture(0)

topmost = []
points = [(200,200)]
while(1):
    _, frame = cap.read()
    final = frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    final = cv2.flip(final, 1)
    #frame = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
    mask = cv2.inRange(frame, (0,70,50),(10,255,225))
    mask = cv2.flip( mask, 1 )
    im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours( mask, contours, 3, (0,255,0), 3)
    cnt = contours[-1]
    topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
    
    points.append(topmost)
    cv2.line(final, points[-1], points[-2], (255,0,0),3)

    cv2.imshow('mask', mask)
    cv2.imshow('img', frame)
    cv2.imshow('final', final)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    time.sleep(0.1)
    

cap.release()
cv2.destroyAllWindows()