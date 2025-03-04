import cv2

image = cv2.imread("image2.png")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    shape = image.shape
    if len(shape) == 2:
        height, width = shape
        channels = 1
    else:
        height, width, channels = shape

    print(f"Wymiary obrazu: {width}x{height}")
    print(f"Liczba kanałów: {channels}")
