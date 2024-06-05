import cv2
from tracker import *

tracker = EuclideanDistTracker()

vid = cv2.VideoCapture("highway.mp4")

object_det = cv2.createBackgroundSubtractorMOG2(history=40,varThreshold=40)


while 1:
    ret, frame = vid.read()
    h,w,_ = frame.shape
    if not ret:
        break
    frame = cv2.resize(frame,(640,640))
    roi = frame[100:550,0:550]
    mask = object_det.apply(roi)
    _,mask = cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    countors , _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    detection = []
    for ctr in countors:
        area = cv2.contourArea(ctr)
        if area >100 :
            # cv2.drawContours(roi,[ctr],-1,(0,255,0))
            x,y,w,h = cv2.boundingRect(ctr)
            
            detection.append([x,y,w,h])
    
    
    boxes_ids = tracker.update(detection)
    for boxes_id in boxes_ids:
        x,y,w,h,id = boxes_id
        cv2.putText(roi,str(id),(x,y-15),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
        cv2.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow("real",frame)
    cv2.imshow("detected",mask)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()