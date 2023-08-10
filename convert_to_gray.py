# Initial setting
import cv2

# Program start
path = 'images/'
# read image
img_color = cv2.imread(path + 'test.jpeg', cv2.IMREAD_COLOR)

if img_color is None:
    print("Read image fail")
    exit(1)

# show readed image on Window
cv2.namedWindow('Color')  # can be dropped
cv2.imshow('Color', img_color)

# Stop running until any key is pressed. '0' means 0ms
cv2.waitKey(0)
# Close window named 'Color'
cv2.destroyWindow('Color')

# Convert img_color object to Gray Scale img
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# cv2.namedWindow('Grayscale')
cv2.imshow('Grayscale', img_gray)


# save(write) img_color object(Gray scale image) to path 'images/' with name 'test_gray.jpeg'
cv2.imwrite(path + 'test_gray.jpeg', img_gray)

cv2.waitKey(0)
# Close all window(s)
cv2.destroyAllWindows()
