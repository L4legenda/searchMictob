import cv2

img = cv2.imread("641100024B-1.jpg")

low = (0, 80, 150)
upper = (70, 255, 255)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

mask = cv2.inRange(hsv, low, upper)

contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

if contours:
    contours = contours[0]
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    cv2.drawContours(img, contours, -1, (255, 0, 0), 3)
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

res = cv2.bitwise_and(img, img, mask=mask)

cv2.imwrite("out.jpg", img)
cv2.imwrite("mask.jpg", mask)
cv2.imwrite("res.jpg", res)
