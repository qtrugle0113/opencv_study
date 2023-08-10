# Initial setting
import cv2

# Test program
path = 'images/'
img_color = cv2.imread(path + 'test.jpeg', cv2.IMREAD_COLOR)

if img_color is None:
    print("Read image fail")
    exit(1)

cv2.namedWindow('Color')  # can be dropped
cv2.imshow('Color', img_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
