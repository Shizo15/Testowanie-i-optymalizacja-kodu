import cv2

image = cv2.imread("image2.png")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    cv2.namedWindow("Obraz", cv2.WINDOW_NORMAL)

    cv2.imshow("Obraz", image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
