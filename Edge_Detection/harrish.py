import cv2
import numpy as np

# Load image and convert to grayscale
image = cv2.imread(r"C:\Users\satwi\Downloads\1.jpg")
image = cv2.resize(image,(640,640),0,0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.09)

# Result is dilated for marking the corners
dst = cv2.dilate(dst, None)

# Threshold to mark the corners
image[dst > 0.01 * dst.max()] = [0, 0, 255]

# Show the result
cv2.imshow('Harris Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
