import cv2

# Load image
image = cv2.imread(r"c:\users\satwi\downloads\4.png")
image = cv2.resize(image,(640,640),0,0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Initiate ORB detector
orb = cv2.ORB_create()

# Detect keypoints
keypoints = orb.detect(gray, None)

# Compute descriptors
keypoints, descriptors = orb.compute(gray, keypoints)

# Draw keypoints
image = cv2.drawKeypoints(image, keypoints, None, color=(0, 255, 0))

# Show the result
cv2.imshow('ORB Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
