import numpy as np
import cv2

image=cv2.imread(r'C:\Users\hp\OneDrive\Desktop\project\test.jpg')
image=cv2.resize(image,(300,300))
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gradients_sobelx=cv2.Sobel(image,-1,1,0)
gradients_sobely=cv2.sobel(image,-1,0,1)
gradients_sobelxy=cv2.addWeighted(gradients_sobelx,0.5.gradients_sobely,0.5)





cv2.imshow('Sobel x',gradients_sobelx)
cv2.imshow('Sobel y',gradients_sobely)
cv2.imshow('Sobel X+Y',gradients_sobelxy)


cv2.imshow('Canny',canny_output)


cv2.waitKey(10000000)