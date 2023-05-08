import numpy
from PIL import Image
import cv2
import os
import PIL
import glob

'''image = Image.open('note.jpg')
print(image.size)

resized_image = image.resize((1655,2339))
resized_image.show('rezize')
img=numpy.array(resized_image)
cv2.imwrite(filename='save.jpg',img=img)
print(resized_image.size)'''


# keep in mind that open CV loads images as BGR not RGB
image = cv2.imread("testmukesh.jpg")
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
cv2.imshow('Image', resizedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
# save the resized image
cv2.imwrite("resize.png", resizedImage, [cv2.IMWRITE_PNG_COMPRESSION, 0])
