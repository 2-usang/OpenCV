import cv2

# ROI(Region of Interest): 관심 영역
img = cv2.imread('./images/sun.jpg')

x = 182
y = 22
w = 123
h = 110

roi = img[y:y+h, x:x+w]
roi_copy = roi.copy()
img[y:y+h, x+w:x+w+w] = roi

# 두 태양을 박스로 감싸기
cv2.rectangle(img, (x, y), (x+w+w, y+h), (0, 255, 0), 3)

cv2.imshow('img', img)
cv2.waitKey()