import cv2
import numpy as np

img = cv2.imread("2.png", cv2.IMREAD_COLOR)
cv2.imshow("wallpaper", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
