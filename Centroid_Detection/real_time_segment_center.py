from ultralytics import YOLO
import cv2
import os
import numpy as np

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
 
# Initialize video capture from an IP camera
video = cv2.VideoCapture(0)
model = YOLO(r"C:\Users\satwi\Downloads\Image_Centroid\Model\yolov8s-seg.pt")
detection = 1
count = 0

while video.isOpened():
    count += 1
    ret, frame = video.read()
    if ret:
        frame = cv2.resize(frame, (640, 640), interpolation=cv2.INTER_LINEAR)
        results = model.track(source=frame, conf=0.35, persist=True)

        if results and results[0].masks is not None:
            masks = results[0].masks.data.cpu().numpy()

            # Create a combined mask of all detected objects
            combined_mask = np.zeros_like(frame[:, :, 0], dtype=np.uint8)
            for mask in masks:
                combined_mask = np.maximum(combined_mask, mask.astype(np.uint8))

            # Create a masked image by applying the combined mask
            masked_image = cv2.bitwise_and(frame, frame, mask=combined_mask)

            # Convert masked image to grayscale
            gray_image = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)

            # Apply thresholding
            _, binary_image = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)

            # Find contours
            contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Calculate centroids and draw them on the image
            for contour in contours:
                # Calculate centroid using moments
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                else:
                    cX, cY = 0, 0

                # Draw centroid on the image
                cv2.circle(masked_image, (cX, cY), 5, (0, 255, 0), -1)

            cv2.imshow("Segmented Image with Centroids", masked_image)
            # cv2.imwrite(f"C:\\Users\\satwi\\Downloads\\main hackaton\\segmented_{count}.jpg", masked_image)
            print(f"Frame {count}: Segmentation applied and image saved.")
        else:
            print(f"Frame {count}: No segmentation masks found.")
        
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()

print("Object detection, segmentation, and centroid calculation completed.")
