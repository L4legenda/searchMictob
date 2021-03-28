import cv2

img = cv2.imread("microb/974.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

low = hsv[25][-25]
up = hsv[25][-25]

mask = cv2.inRange(hsv, low, up)

contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours = contours[0]

count = len(contours) - 1

for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 1)

print(count)

cv2.imwrite("hsv.png", hsv)
cv2.imwrite("mask.png", mask)


cv2.imshow("Display window", img)

k = cv2.waitKey(0)
if k == ord("q"):
    cv2.imwrite("res.png", img)
