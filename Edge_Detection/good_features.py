import cv2
import numpy as np

# Load image and convert to grayscale
image = cv2.imread(r"c:\users\satwi\downloads\2.jpg")
image = cv2.resize(image,(640,640),0,0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect Shi-Tomasi corners
corners = cv2.goodFeaturesToTrack(gray, 4, 0.01, 10)
corners = np.int0(corners)

# Draw corners on the image
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (x, y), 3, 255, -1)

# Show the result
cv2.imshow('Shi-Tomasi Corner\s', gray)
cv2.imshow('Shi-Tomasi Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
