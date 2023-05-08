#working one
import cv2
import numpy as np
from ocr import *
'''
# read the image
image = cv2.imread('save.jpg')
# convert the image to grayscale format
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# apply binary thresholding
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# draw contours on the original image
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                 lineType=cv2.LINE_AA)

cv2.imshow('None approximation', image_copy)
cv2.waitKey(0)
cv2.imwrite('contours_none_image1.jpg', image_copy)
cv2.destroyAllWindows()
'''
"""
Contour detection and drawing using different extraction modes to complement
the understanding of hierarchies
"""
'''image2 = cv2.imread('ROI.png')
img_gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
ret, thresh2 = cv2.threshold(img_gray2, 150, 255, cv2.THRESH_BINARY)'''

'''contours3, hierarchy3 = cv2.findContours(thresh2, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
image_copy4 = image2.copy()
cv2.drawContours(image_copy4, contours3, -1, (0, 255, 0), 2, cv2.LINE_AA)
# see the results
cv2.imshow('LIST', image_copy4)
print(f"LIST: {hierarchy3}")
cv2.waitKey(0)
cv2.imwrite('contours_retr_list.jpg', image_copy4)
cv2.destroyAllWindows()
'''
'''contours4, hierarchy4 = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
image_copy5 = image2.copy()
cv2.drawContours(image_copy5, contours4, -1, (0, 255, 0), 2, cv2.LINE_AA)
# see the results
cv2.imshow('EXTERNAL', image_copy5)
#print(contours4)
#print(f"EXTERNAL: {hierarchy4}")
cv2.waitKey(0)
cv2.imwrite('contours_retr_external.jpg', image_copy5)
cv2.destroyAllWindows()''' #last

'''image = cv2.imread("sheet.jpg")
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

## RESIZE IMAGE
# scale in percentage
scale = 60
newWidth = int(image.shape[1] * scale / 100)
newHeight = int(image.shape[0] * scale / 100)
newDimension = (newWidth, newHeight)
# resize image
resizedImage = cv2.resize(image, newDimension, interpolation=cv2.INTER_AREA)
grayImage=cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)
#estimatedThreshold, thresholdImage=cv2.threshold(grayImage,90,255,cv2.THRESH_BINARY)
estimatedThreshold, thresholdImage=cv2.threshold(grayImage,90,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(thresholdImage, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# make a copy of the resized image since we are going to draw contours on the resized image
resizedImageCopy = np.copy(resizedImage)

# draw all contours with setting the parameter to -1
# but if you use this function, you should comment the for loop below
# cv2.drawContours(resizedImageCopy,contours,-1,(0,0,255),2)
# filter contours
for i, c in enumerate(contours):
    areaContour = cv2.contourArea(c)
    if areaContour < 2000 or 100000 < areaContour:
        continue
    cv2.drawContours(resizedImageCopy, contours, i, (255, 10, 255), 4)
#cv2.imshow('Image', resizedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
# save the resized image
cv2.imwrite("result.png", resizedImageCopy, [cv2.IMWRITE_PNG_COMPRESSION, 0])'''


'''#thresh = cv2.threshold(img_gray2, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]

# Find contour and sort by contour area
cnts = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

# Find bounding box and extract ROI
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    ROI = image2[y:y+h, x:x+w]
    break

cv2.imshow('ROI',ROI)
cv2.imwrite('ROI.png',ROI)
cv2.waitKey() #super result=ROI.png'''

'''import cv2
import numpy as np


# load image as grayscale
img = cv2.imread('resize.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold input image using otsu thresholding as mask and refine with morphology
ret, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel = np.ones((9,9), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# put mask into alpha channel of result
result = img.copy()
result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
result[:, :, 3] = mask

# save resulting masked image
cv2.imwrite('result.png', result)'''
cropper('testmukesh.jpg')
cv2.waitKey(0)
cv2.destroyAllWindows()