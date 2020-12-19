from normalization import Normalization
import cv2

image = cv2.imread('test.jpg', 0)
norm = Normalization()
normalized_image = norm.normalize_image(image, 0, 1)

cv2.imshow('Window', normalized_image)
cv2.waitKey()
cv2.destroyAllWindows()


