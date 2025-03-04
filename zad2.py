import cv2

image = cv2.imread("image2.png", cv2.IMREAD_COLOR)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    height, width, channels = image.shape
    print(f"Liczba kanałów: {channels}")
