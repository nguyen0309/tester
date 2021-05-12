import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("Untitled.bmp")
#img = np.zeros((200,200), np.uint8)
#cv.rectangle(img, (0, 100), (200, 200), (255), -1)
#cv.rectangle(img, (0, 50), (100, 100), (127), -1)
b, g, r = cv.split(img)
cv.imshow("img", img)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)

plt.hist(b.ravel(), 255, [0, 255])
plt.hist(g.ravel(), 255, [0, 255])
plt.hist(r.ravel(), 255, [0, 255])

hist = cv.calcHist([img], [0], None, [255], [0, 255])
plt.plot(hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
 