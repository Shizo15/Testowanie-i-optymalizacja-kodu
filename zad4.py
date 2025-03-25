import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

height, width = image.shape[:2]
new_width = int(width * 3)
new_height = int(height * 3)
resized = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
cv2.imshow("INTER_LINEAR", resized)
resized2 = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
cv2.imshow("INTER_CUBIC", resized2)
resized3 = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_NEAREST)
cv2.imshow("INTER_NEAREST", resized3)
resized4 = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("INTER_LANCZOS4", resized4)


cv2.waitKey(0)