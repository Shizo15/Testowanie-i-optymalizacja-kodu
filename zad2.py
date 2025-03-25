import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

height, width = image.shape[:2]
new_width = int(width * 2)
new_height = int(height * 2)
resized = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

cv2.imshow("Resized", resized)
cv2.waitKey(0)