import os
import cv2


img_path = os.path.join('.', 'img1.jpg')

img = cv2.imread(img_path)

cv2.imwrite(os.path.join('.', 'img1_output.jpg'), img)

cv2.imshow('image', img)
cv2.waitKey(0)