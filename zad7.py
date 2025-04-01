import cv2
import numpy as np

image = cv2.imread('image.jpg')

h, w = image.shape[:2]
tile_h, tile_w = h // 3, w // 3

for i in range(3):
    for j in range(3):
        tile = image[i * tile_h: (i + 1) * tile_h,
               j * tile_w: (j + 1) * tile_w]

        cv2.imshow(f'Czesc {i * 3 + j + 1}', tile)
        cv2.waitKey(700)

cv2.destroyAllWindows()