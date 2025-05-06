import cv2

image = cv2.imread("image.jpg")

params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
for d, sc, ss in params:
    blurred = cv2.bilateralFilter(image, d, sc, ss)
    cv2.imshow(f"Bilateral d={d}, sc={sc}, ss={ss}", blurred)
    cv2.waitKey(0)

# 3d: Odpowiedzi
# i. Tak, redukuje szum przy zachowaniu krawędzi.
# ii. Tak, lepiej niż metody uśredniające.
# iii. Najlepsze: d=11, sc=75, ss=75 (eksperymentalnie).