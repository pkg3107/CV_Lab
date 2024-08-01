import cv2 as cv

width=600
height=300

src=cv.imread('/home/student/Documents/220962250_CV/Week2/flower.jpeg')

resized=cv.resize(src, (width, height), interpolation=cv.INTER_LINEAR)
cropped=src[0:190, 35:250]

cv.imshow('Original Image', src)
cv.imshow('Resized Image', resized)
cv.imshow('Cropped Image', cropped)

cv.waitKey(0)
