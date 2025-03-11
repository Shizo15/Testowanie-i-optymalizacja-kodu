import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]


x = int(input("Podaj współrzędne x: "))

y = int(input("Podaj współrzędne y: "))

if int(x)>=w or int(y)>=h:
    raise ValueError("Obraz jest za mały! Współrzędne wychodzą poza obszar obrazu.")

else:
    image[x, y] = (0, 0, 0)
    print("Zmieniono pixel o podanych współrzęndych")

cv2.imshow("Image", image)
cv2.waitKey(0)