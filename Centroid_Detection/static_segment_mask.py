from ultralytics import YOLO
import cv2
import os
import numpy as np

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

model = YOLO(r"C:\Users\satwi\Downloads\Image_Centroid\Model\yolov8s-seg.pt")

img = cv2.imread(r"C:\Users\satwi\Downloads\1.jpg")
img = cv2.resize(img, (640, 640), interpolation=cv2.INTER_LINEAR)

results = model.track(source=img, conf=0.5, persist=True)

masks = results[0].masks.data.cpu().numpy() if results[0].masks is not None else []

combined_mask = np.zeros_like(img[:, :, 0], dtype=np.uint8)
for mask in masks:
    combined_mask = np.maximum(combined_mask, mask.astype(np.uint8))

masked_image = cv2.bitwise_and(img, img, mask=combined_mask)

cv2.imshow("Segmented Image", masked_image)
# cv2.imwrite("C:\\Users\\satwi\\Downloads\\main hackaton\\segmented_laptop.jpg", masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Object detection and segmentation completed.")
