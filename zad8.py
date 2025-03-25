import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

height, width = image.shape[:2]
new_width = int(width * 4)
new_height = int(height * 4)

resized = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
cv2.imshow("CUBIC", resized)

resized1 = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("LANCZOS4", resized1)
cv2.waitKey(0)