import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

for scale in range(100,320,20):
    width = int(image.shape[1] * scale / 100)
    height = int(image.shape[0] * scale / 100)
    resized = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)

    cv2.imshow(f"Skala: {scale}%", resized)
    cv2.waitKey(500)


