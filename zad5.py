import cv2

image = cv2.imread('image.jpg')
height, width = image.shape[:2]

x_start = width // 2  #
cropped = image[:, x_start:width]  

flipped = cv2.flip(cropped, 1)

image[:, x_start:width] = flipped

cv2.imshow('Oryginal z odbitym fragmentem', image)
cv2.waitKey(0)


