import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype=np.uint8)

print("Podaj wartości startX, startY, endX, endY: ")
startY=input("StartY: ")
endY=input("EndY: ")
startX=input("StartX: ")
endX=input("EndX: ")


roi = image[int(startY):int(endY),int(startX):int(endX)]
roi[:] = (0, 255, 0)

image_with_roi = image.copy()

cv2.imshow('Obraz z zaznaczonym ROI podadnym przez uzytkownika', image_with_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow('Oryginalny obraz', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()