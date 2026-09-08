import os

import cv2

img_path = os.path.join('.', 'bird.png')

img = cv2.imread(img_path)

k_size = 7
img_blur = cv2.blur(img, (k_size, k_size))
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 3)
img_median_blur = cv2.medianBlur(img, k_size)

cv2.imshow('image', img)
cv2.imshow('image blur', img_blur)
cv2.imshow('image gaussian blur', img_gaussian_blur)
cv2.imshow('image median blur', img_median_blur)
cv2.waitKey(0)