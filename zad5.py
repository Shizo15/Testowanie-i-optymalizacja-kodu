import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]

tl = image[0:h//2, 0:w//2]
tr = image[0:h//2, w//2:w]
br = image[h//2:h, w//2:w]
bl = image[h//2:h, 0:w//2]


image[0:h // 2, 0:w // 2] = (255,0,0)

cv2.imshow("Corner", image)
cv2.waitKey(0)

