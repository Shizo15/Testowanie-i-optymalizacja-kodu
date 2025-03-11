import cv2

image = cv2.imread('image.jpg')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)

print(f"Najjaśniejszy piksel ma jasność: {max_val}")
print(f"Współrzędne najjaśniejszego piksela: {max_loc}")

cv2.circle(image, max_loc, 5, (0, 0, 255), -1)

cv2.imshow("Najjasniejszy piksel", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
