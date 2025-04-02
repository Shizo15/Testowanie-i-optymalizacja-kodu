import cv2

image = cv2.imread('image.jpg')

B, G, R = cv2.split(image)

R = cv2.add(R, 30)
G = cv2.subtract(G, 20)
B = cv2.add(B, 10)

filtered_image = cv2.merge([B, G, R])

cv2.imshow('Filtered', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
