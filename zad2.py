import cv2

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]

center = (w // 2, h // 2)

rotation_matrix = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

cv2.imshow('Oryginalny obraz', image)
cv2.imshow('Obrocony obraz o -90 stopni', rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()