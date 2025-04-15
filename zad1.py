import cv2

image = cv2.imread('binarny.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

eroded_square = cv2.erode(gray, square, iterations=1)
eroded_ellipse = cv2.erode(gray, ellipse, iterations=1)

cv2.imshow('Oryginal', image)
cv2.imshow('Eroded square', eroded_square)
cv2.imshow('Eroded ellipse', eroded_ellipse)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Erozja powoduje zmniejszenie obiektów na obrazie. Element kwadratowy daje bardziej jednolite zmniejszenie we wszystkich kierunkach,
# podczas gdy element eliptyczny może zachowywać się nieco inaczej na krawędziach o różnej krzywiźnie.
# Małe obiekty mogą całkowicie zniknąć, a większe stają się cieńsze.