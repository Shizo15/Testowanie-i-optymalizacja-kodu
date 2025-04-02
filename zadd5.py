import cv2

image1 = cv2.imread('image.jpg')
image2 = cv2.imread('image1.jpg')

diff = cv2.absdiff(image1, image2)

cv2.imshow('Difference', diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
