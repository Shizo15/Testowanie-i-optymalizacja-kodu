import cv2
import imutils


image = cv2.imread("image.jpg")
for angle in range(0,361,15):
    shifted_image = imutils.rotate(image, angle)
    cv2.imshow(f"Obrocony obraz o {angle} stopni", shifted_image)

    cv2.waitKey(500)
