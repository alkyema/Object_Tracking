from ultralytics import YOLO
import cv2
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Initialize video capture from an IP camera
# video = cv2.VideoCapture("http://192.0.0.4:8080/video")
video = cv2.VideoCapture(0)
model = YOLO(r"C:\Users\satwi\Downloads\Image_Centroid\Model\yolov8s-seg.pt")
detection = 1
count = 0

while video.isOpened():
    count += 1
    ret, frame = video.read()
    if ret:
        frame = cv2.resize(frame, (640, 640), 0, 0)
        results = model.track(source=frame, conf=0.35, persist=True)

        img_with_boxes = results[0].plot()
        for box in results[0].boxes:
            # Move tensor to CPU before converting to NumPy
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            centroid_x = int((x1 + x2) / 2)
            centroid_y = int((y1 + y2) / 2)

            cv2.circle(img_with_boxes, (centroid_x, centroid_y), 5, (0, 255, 0), -1)
            print(f"Centroid: ({centroid_x}, {centroid_y})")
        cv2.imshow("frame", img_with_boxes)
        print(detection)
        # Uncomment and adjust the following lines to save images if needed
        # if detection:
        #     path1 = "C:\\Users\\satwi\\Downloads\\main hackaton\\save\\detected"+str(count)+".jpg"
        #     path2 = "C:\\Users\\satwi\\Downloads\\main hackaton\\save\\real"+str(count)+".jpg"
        #     cv2.imwrite(path1, img_with_boxes)
        #     cv2.imwrite(path2, frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()

print("Object detection prediction completed.")
