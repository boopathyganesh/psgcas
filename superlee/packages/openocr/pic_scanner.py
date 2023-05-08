import cv2
import numpy as np
from ocr import scan
def resize(image):
        image = cv2.imread(image)
        ## RESIZE IMAGE
        # scale in percentage
        scale = 60
        newWidth = int(image.shape[1] * scale / 100)
        newHeight = int(image.shape[0] * scale / 100)
        newDimension = (newWidth, newHeight)
        # resize image
        resizedImage = cv2.resize(image, newDimension, interpolation=cv2.INTER_AREA)
        cv2.imshow('Image', resizedImage)
        cv2.imwrite('resize.png', resizedImage)

def pic_crop(image):
    img=cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # threshold input image using otsu thresholding as mask and refine with morphology
    ret, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((9, 9), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # put mask into alpha channel of result
    result = img.copy()
    result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
    result[:, :, 3] = mask

    # save resulting masked image
    cv2.imwrite('result.png', result)
    roi('result.png')
def roi(img):
    img=cv2.imread(img)
    img_gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(img_gray2, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]

    # Find contour and sort by contour area
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    # Find bounding box and extract ROI
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        ROI = img[y:y + h, x:x + w]
        break

    cv2.imshow('ROI', ROI)
    cv2.imwrite('ROI.png', ROI)
    cv2.waitKey()  # super result=ROI.png
if __name__ == '__main__':

    resize('sheet1.jpg')
    pic_crop('resize.png')
    roi('result.png')
    scan('ROI.png')
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # save the resized image