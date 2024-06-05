import cv2

# Load image
image = cv2.imread(r"c:\users\satwi\downloads\2.jpg")
image = cv2.resize(image, (640, 640))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# Detect keypoints
keypoints = fast.detect(gray, None)

# Sort keypoints based on response and select the top 4
keypoints = sorted(keypoints, key=lambda x: -x.response)[:4]

# Draw keypoints
image = cv2.drawKeypoints(image, keypoints, None, color=(255, 0, 0))

# Show the result
cv2.imshow('FAST Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
