import cv2
import numpy as np

image1 = cv2.imread('/home/student/Documents/220962250_CV/Week2/photo.jpeg')
image2 = cv2.imread('/home/student/Documents/220962250_CV/Week2/flower.jpeg')

gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

hist1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([gray_image2], [0], None, [256], [0, 256])

cv2.normalize(hist1, hist1, 0, 1, cv2.NORM_MINMAX)
cv2.normalize(hist2, hist2, 0, 1, cv2.NORM_MINMAX)

cdf1 = np.cumsum(hist1)
cdf2 = np.cumsum(hist2)

result_image = np.zeros_like(gray_image1)
for i in range(256):
    result_image[gray_image1 == i] = np.round(255 * cdf2[np.searchsorted(cdf1, hist1[i])])

result_image = result_image.astype(np.uint8)

cv2.imshow('Original Image', image1)
cv2.imshow('Image for Histogram Comparision', image2)
cv2.imshow('Result Image', result_image)

cv2.waitKey(0)
cv2.destroyAllWindows()