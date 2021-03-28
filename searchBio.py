import cv2

img = cv2.imread("microb/9-qma4eOXWg.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lowH = 100
lowS = 0
lowV = 100

while True:
    low = (lowH, lowS, lowV)
    upper = (180, 255, 255)
    mask = cv2.inRange(hsv, low, upper)
    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('frame', res)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours = contours[0]

if contours:
    cv2.drawContours(img, contours, -1, (255, 0, 0), 2)

cv2.imwrite("hsv.jpg", hsv)
cv2.imwrite("mask.jpg", mask)
cv2.imwrite("res.jpg", res)
cv2.imwrite("gray.jpg", gray)
