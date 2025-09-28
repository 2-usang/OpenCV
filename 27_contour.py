import cv2
import random
import numpy as np

# 외곽선
# 영상에서 같은 색 또는 강도를 가진 경계선을 추적해 얻는 좌표 집합
# 영상 분석에서 물체의 모양, 크기, 위치를 찾을 때 유용

img1 = cv2.imread('./images/contours.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('./images/milkdrop.bmp', cv2.IMREAD_GRAYSCALE)

_, img_bin1 = cv2.threshold(img1, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
_, img_bin2 = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]

dst1 = np.zeros((h1, w1, 3), np.uint8)
dst2 = np.zeros((h2, w2, 3), np.uint8)

# cv2.RETR_CCOMP : 외곽선 추출 방식. 2계층 구조로 모든 컨투어 추출
#   cv2. RETR_EXTERNAL : 최외곽 외곽선만 추출

# cv2.CHAIN_APPROX_NONE : 외곽선 근사화 방식. 모든 경계 좌표 저장
#   cv2.CHAIN_APPROX_SIMPLE : 직선 구간은 시작/끝만 저장(효율적)

# contours1 : 외곽선의 좌표 목록(리스트)
# hierarchy1  :계층 관계를 나타내는 배열
#   hierarchy1[0][i] = [next, prev, child, parent]
#   next : 같은 계층 레벨에서 다음 외곽선의 인덱스(없으면 -1)
#   prev : 같은 계층 레벨에서 이전 외곽선의 인덱스(없으면 -1)
#   child  : 하위(내부) 외곽선의 인덱스(없으면 -1)
#   parent : 상위(외부) 외곽선의 인덱스(없으면 -1)

contours1, hierarchy1 = cv2.findContours(img1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

print(contours1)
print('-'*50)
print(hierarchy1)

contours2, _ = cv2.findContours(img_bin2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
dst1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

cv2.drawContours(dst1, contours1, -1, color, 3) # -1 : 외곽선 한번에 다 그려줘

for i in range(len(contours2)):
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    cv2.drawContours(dst2, contours2, i, color, 3)  # i : 하나씩 그려줘

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()