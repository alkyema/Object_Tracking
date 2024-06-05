import cv2

vid = cv2.VideoCapture("4.mp4")

def tracker_selector():
    #1)KCF best 2)CSRT 3)medianflow 4)TLD
    choice = '2'
    
    if choice == '0':
        tracker = cv2.legacy.TrackerBoosting_create()
    if choice == '1':
        tracker = cv2.legacy.TrackerMIL_create()
    if choice == '2':
        tracker = cv2.legacy.TrackerKCF_create()
    if choice == '3':
        tracker = cv2.legacy.TrackerTLD_create()
    if choice == '4':
        tracker = cv2.legacy.TrackerMedianFlow_create()
    if choice == '5':
        tracker = cv2.legacy.TrackerGOTRUN_create()
    if choice == '6':
        tracker = cv2.legacy.TrackerMOSSE_create()
    if choice == '7':
        tracker = cv2.legacy.TrackerCSRT_create()
        
    return tracker


tracker = tracker_selector()
tracker_name = str(tracker).split()[0][1:]

ret,frame = vid.read()
frame = cv2.resize(frame,(640,640))
bbox = cv2.selectROI("Tracing",frame,False)
tracker.init(frame,bbox)

def drawbox(img,bbox):
    x,y,w,h = map(int,bbox)
    cv2.rectangle(img,(x,y),(x+w,(y+h)),(255,0,0),3)
    cv2.putText(frame,"tracking",(0,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(255,0,0))

    pass

while 1:
    timer = cv2.getTickCount()
    ret,frame = vid.read()
    frame = cv2.resize(frame,(640,640))
    ret,bbox = tracker.update(frame)
    if ret:
        drawbox(frame,bbox)
    else:
        cv2.putText(frame,"lost",(0,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(255,0,0))
    fps = cv2.getTickFrequency()//(cv2.getTickCount()-timer)
    cv2.putText(frame,"FPS: "+str(fps),(0,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(255,0,0))
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()