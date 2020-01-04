import numpy as np
import cv2

imgpath = "C:\\Users\\DEAN OF COLNAS\\Desktop\\images\\coins.png"
image = cv2.imread(imgpath, 1)

r = 500.0 / image.shape[1]
dim = (500, int(image.shape[0] * r))

#image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

img2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  

blurred = cv2.GaussianBlur(img2, (11, 11), 0)
cv2.imshow("Image", image)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)
cv2.waitKey(0)


(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("I count %d coins in this image" % (len(cnts)))

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)

cv2.imshow("Coins", coins)
cv2.waitKey(0)