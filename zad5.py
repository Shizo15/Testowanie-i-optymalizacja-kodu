import cv2

image1 = cv2.imread("image2.png")
image2 = cv2.imread("image2_gray.png")

if image1 is None or image2 is None:
    print("Błąd: Nie można wczytać jednego z obrazów!")
else:
    cv2.imshow("Obraz 1", image1)
    cv2.imshow("Obraz 2", image2)

    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

    cv2.destroyAllWindows()
