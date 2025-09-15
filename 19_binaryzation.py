'''
3. 영상의 이진화

이진화(Binary Thresholding) 는 영상을 흑백(0 또는 255)으로 변환하여 특정 임계값(threshold) 이상인 픽셀을 흰색(255)으로, 이하인 픽셀을 검은색(0)으로 변환하는 과정입니다. 이는 객체 검출, OCR(광학 문자 인식), 엣지 검출 등의 전처리 과정에서 중요한 역할을 합니다. OpenCV에서는 cv2.threshold() 함수를 사용하여 고정 임계값 이진화, 적응형 이진화, Otsu의 이진화 등을 적용할 수 있습니다. 특히, cv2.THRESH_BINARY는 기본적인 이진화 방법이며, cv2.ADAPTIVE_THRESH_GAUSSIAN_C는 조명이 균일하지 않은 경우에도 효과적으로 이진화를 수행할 수 있습니다.

오츠 이진화

오츠 이진화(Otsu's Binarization) 는 OpenCV에서 제공하는 자동 임계값 결정 기법으로, 영상의 히스토그램을 분석하여 객체와 배경을 가장 잘 구분할 수 있는 최적의 임계값을 자동으로 찾는 방법입니다. 이는 cv2.THRESH_OTSU 옵션을 사용하여 cv2.threshold() 함수에서 적용할 수 있으며, 특히 배경과 객체 간의 명암 대비가 뚜렷한 경우 효과적으로 동작합니다. 오츠 이진화는 모든 픽셀 값의 분포를 기반으로 클래스 내 분산(intra-class variance)을 최소화하는 임계값을 자동으로 선택하여 수동으로 임계값을 설정하는 불편함을 줄여줍니다. 일반적으로 cv2.THRESH_BINARY + cv2.THRESH_OTSU를 함께 사용하여 이진화를 수행하며, 그레이스케일 변환이 선행되어야 합니다.
'''

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/cells.png', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 255])

a, dst1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
# 임계값 100으로 설정, 이거보다 크면 255로 변환.
# 넘지 않으면 검정(0)
# a 는 threshold => 100
print(a)

b, dst2 = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)
print(b)
c, dst3 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# otsu 에 아무 숫자나 넣어줘도 됨
# otsu -> 자동 임계값 결정 기법 
print(c)

plt.plot(hist)
plt.show()

cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey()