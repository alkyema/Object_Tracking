from ultralytics import YOLO
import cv2
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Load the YOLO model
model = YOLO(r"C:\Users\satwi\Downloads\yolov8s-seg.pt")

# Read and resize the image
img = cv2.imread(r"C:\Users\satwi\Downloads\main hackaton\5.jpg")
img = cv2.resize(img, (640, 640), interpolation=cv2.INTER_LINEAR)

# Perform detection
results = model.track(source=img, conf=0.35, persist=True)

print(results)
# Draw the bounding box on the image
img_with_boxes = results[0].plot()

# Calculate the centroid of the detected object(s)
for box in results[0].boxes:
    x1, y1, x2, y2 = box.xyxy[0].numpy() 
    print(x1,y1,x2,y2)# Get the coordinates of the bounding box
    centroid_x = int((x1 + x2) / 2)
    centroid_y = int((y1 + y2) / 2)
    
    # Draw the centroid on the image
    cv2.circle(img_with_boxes, (centroid_x, centroid_y), 5, (0, 255, 0), -1)
    print(f"Centroid: ({centroid_x}, {centroid_y})")

# Show the image with the bounding box and centroid
cv2.imshow("frame", img_with_boxes)
cv2.imwrite("C:\\Users\\satwi\\Downloads\\main hackaton\\det5.jpg", img_with_boxes)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Object detection and centroid calculation completed.")
