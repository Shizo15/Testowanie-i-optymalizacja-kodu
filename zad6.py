import cv2

image = cv2.imread("image.jpg")

left_eye_center = (115, 80)
right_eye_center = (155, 80)
eye_radius = 8

mouth_top_left = (110, 120)
mouth_bottom_right = (160, 140)

face_center = (130, 90)
face_radius = 60

cv2.circle(image, left_eye_center, eye_radius, (0, 0, 255), -1)
cv2.circle(image, right_eye_center, eye_radius, (0, 0, 255), -1)

cv2.rectangle(image, mouth_top_left, mouth_bottom_right, (0, 255, 0), -1)

cv2.circle(image, face_center, face_radius, (255, 0, 0), 2)

cv2.imshow("Zamazane zdjecie", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
