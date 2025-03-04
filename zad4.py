import cv2

image_gray = cv2.imread("image2.png", cv2.IMREAD_GRAYSCALE)

if image_gray is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    cv2.imwrite("image2_gray.png", image_gray)
    print("Obraz zapisano jako 'imag2e_gray.png'")
