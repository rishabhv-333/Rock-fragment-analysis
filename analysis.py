# Rishabh Verma
import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.morphology import disk
from skimage import filters
import warnings
warnings.filterwarnings("ignore")
f = open("data.txt","w")
image = cv2.imread("sample.jpg", 0)
originalimage = cv2.imread("sample.jpg",0)
#thresholding and filter
selem = disk(5)
median = filters.rank.mean(image, selem = selem)
blur = cv2.GaussianBlur(median, (5,5),0)
(thresh, img) = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY |
cv2.THRESH_OTSU)
sobel = filters.sobel(img)
selem = disk(5)
med = filters.rank.mean(sobel, selem = selem)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
opening = cv2.morphologyEx(med,cv2.MORPH_OPEN, kernel)
contours, hierarchy = cv2.findContours(opening,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image2 = cv2.drawContours(opening, contours, -1, (0,255,255), 3)

#generating contour and finding its area
a=0
count = 0
for i in contours:
    area = cv2.contourArea(i)
    a += area
    count += 1
k = a/count

for i in contours:
    area = cv2.contourArea(i)
    if area >= k and area<=5*k:
        f.write(str(area) + "\n")

mask = np.ones(image.shape[:2], dtype="uint8") * 255
count1 = 0
for c in contours:
    if cv2.contourArea(c)<k:
        cv2.drawContours(mask, [c], -1, 0, -1)
        count1 += 1
image = cv2.bitwise_and(image2, image2, mask = mask)

#shows image window
cv2.namedWindow("original image",cv2.WINDOW_NORMAL)
cv2.resizeWindow("original image", 600,600)
cv2.imshow("original image", originalimage)
cv2.namedWindow("intermediate",cv2.WINDOW_NORMAL)
cv2.resizeWindow("intermediate", 600,600)
cv2.imshow("intermediate", img)
cv2.namedWindow("final",cv2.WINDOW_NORMAL)
cv2.resizeWindow("final", 600,600)
cv2.imshow("final", image)

##can be used if we need output in same window
# joinimg=np.concatenate((img,image),axis=1)
# cv2.imshow('blast fragment analysis',joinimg)
##

f.close()
cv2.waitKey(0)
cv2.destroyAllWindows()
