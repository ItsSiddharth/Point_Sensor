import cv2
import os
import time

path = 'E:\LiveED\Dataset'

cap = cv2.VideoCapture(0)
i = 0
t = time.time()

while(time.time() - t < 5):
    _,frame = cap.read()
    resized = cv2.resize(frame,(100,100))
    cv2.imwrite(os.path.join(path,'image%d.jpg'%i),resized)
    i = i + 1


cap.release()
cv2.destroyAllWindows()

