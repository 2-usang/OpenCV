import cv2
import math

def setLabel(img, pts, label):
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (0,0, 255), 2)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))


img = cv2.imread('./images/polygon.bmp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, img_bin1 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
_, img_bin2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
# INV -> 반대로 나옴 (배경이 검, 객체가 흰색일 때 훨씬 잘 찾음)

contours, _ = cv2.findContours(img_bin2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for pts in contours:
    if cv2.contourArea(pts) < 50:
        continue
    
    # approxPolyDP : 꼭짓점의 개수를 줄여 간단한 규치 기반 분류
    # cv2.arcLength(pts, True)*0.02 : 결과가 작을수록 원본과 비슷(정밀), 클수록 단순화
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)    # True : 폐곡선이 아닐시에 폐곡선으로 만듦
    vtc = len(approx)
    print(vtc)

    if vtc == 3:
        setLabel(img, pts, 'TRI')

    elif vtc == 4:
        setLabel(img, pts, 'RECT')

    else:
        length = cv2.arcLength(pts, True)
        area = cv2.contourArea(pts)
        # 4*math.pi * area/(length*length): 원형도를 구함
        # 값의 범위 : 0~1, 1에 가까울수록 원에 가까움
        ratio = 4. * math.pi * area / (length * length)
        if ratio > 0.8:
            setLabel(img, pts, 'CIR')
        else:
            setLabel(img, pts, 'NONAME')

cv2.imshow('img', img)
cv2.imshow('img_bin1', img_bin1)
cv2.imshow('img_bin2', img_bin2)
# cv2.imshow('gray', gray)
cv2.waitKey()