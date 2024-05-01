import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Read image. 
img = cv2.imread('ImgsToTest/img231003152309.jpg', cv2.IMREAD_COLOR) 
#cv2.imshow('Preview',img)
#cv2.waitKey(0)

#red = img[:,:,2]
  
# Convert to grayscale. 
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
blurred = cv2.blur(grey,(3,3))
# Blur using 3 * 3 kernel. 
#gray_blurred = cv2.blur(HSV, (3, 3)) 

#cv2.imshow("ProgramInput",red)
#cv2.waitKey(0)
  
# Apply Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(blurred,  
                   cv2.HOUGH_GRADIENT, dp=1.5, minDist=20, param1 = 50, 
               param2 = 45, minRadius = 20, maxRadius = 35) #tune min/max radius first 
print(detected_circles)
# Draw circles that are detected. 
if detected_circles is not None: 
    #print("Inside")
  
    # Convert the circle parameters a, b and r to integers. 
    detected_circles = np.uint16(np.around(detected_circles)) 
  
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 
  
        # Draw the circumference of the circle. 
        cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
  
        # Draw a small circle (of radius 1) to show the center. 
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3) 
    cv2.imshow("Detected Circle", img) 
    cv2.waitKey(0)     

