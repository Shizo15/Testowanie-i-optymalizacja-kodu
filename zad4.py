import cv2

image = cv2.imread('image.jpg')


(h, w) = image.shape[:2]

center = (w // 2, h // 2)

try:
    angle = float(input("Podaj kąt obrotu (w stopniach): "))
except ValueError:
    print("Nieprawidłowa wartość kąta. Użyj liczby.")
    exit()

scale = 1.0
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

cv2.imshow('Oryginalny obraz', image)
cv2.imshow('Obrócony obraz', rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()