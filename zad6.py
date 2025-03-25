import cv2

image = cv2.imread('image.jpg')

print("\nWybierz sposób odbicia:")
print("0 - pionowe")
print("1 - poziome")
print("-1 - pionowe i poziome (oba)")

while True:
    try:
        flip_code = int(input("Twój wybór (0, 1 lub -1): "))
        if flip_code in [0, 1, -1]:
            break
        else:
            print("Proszę wybrać 0, 1 lub -1.")
    except ValueError:
        print("To nie jest liczba. Spróbuj ponownie.")

flipped_image = cv2.flip(image, flip_code)

cv2.imshow('Oryginalny obraz', image)
cv2.imshow('Odbity obraz', flipped_image)


cv2.waitKey(0)
cv2.destroyAllWindows()