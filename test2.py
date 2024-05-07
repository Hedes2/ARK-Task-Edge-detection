import cv2
import numpy as np

# Load left and right camera images
left_img = cv2.imread(r'C:\Users\hp\Desktop\project_env\files\test1.png',0)
right_img = cv2.imread(r'C:\Users\hp\Desktop\project_env\files\test2.png',0)

# Perform Block Matching stereo correspondence
block_size=11
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(left_img, right_img)

# Normalize the disparity map
normalized_disparity = cv2.normalize(disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Create a color map for visualization
colormap = cv2.applyColorMap(normalized_disparity, cv2.COLORMAP_JET)

# Display the depth map
cv2.imshow('Depth Map', colormap)
cv2.waitKey(0)
cv2.destroyAllWindows()
