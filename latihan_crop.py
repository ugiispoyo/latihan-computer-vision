import os

import cv2

img = cv2.imread(os.path.join(".", "img1.jpg"))

print(img.shape)

croped_img = img[120:300, 200:600]

print(croped_img)

cv2.imshow('img', img)
cv2.imshow('croped', croped_img)
cv2.waitKey(0)