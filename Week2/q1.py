import cv2 as cv

img=cv.imread('/home/student/Documents/220962250_CV/Week2/photo.jpeg')

src=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
final_img=cv.equalizeHist(src)

cv.imshow('Original Image',src)
cv.imshow('Equalised Image',final_img)
cv.waitKey(0)