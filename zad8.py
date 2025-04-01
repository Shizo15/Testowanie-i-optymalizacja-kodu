import cv2
import numpy as np

image = cv2.imread('image.jpg')

w = image.shape[1]
starX=0
endX=400
startY=70
endY=470
step = 10

while True:
    if endX > w:
        break  # Zakończ, jeśli koniec obrazu

    roi = image[startY:endY, starX:endX]

    # Wyświetl ROI
    cv2.imshow("Przesuwające się ROI", roi)

    key = cv2.waitKey(0)

    starX += step
    endX += step


cv2.destroyAllWindows()