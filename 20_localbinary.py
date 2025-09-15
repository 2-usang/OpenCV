'''
적응형 이진화
적응형 이진화(Adaptive Thresholding) 는 OpenCV에서 제공하는 이진화 기법 중 하나로, 조명 변화가 심한 영상에서도 적절한 임계값을 적용하여 이진화를 수행하는 방법입니다. 일반적인 cv2.threshold()는 하나의 고정된 임계값을 사용하지만, cv2.adaptiveThreshold()는 영상의 작은 영역마다 서로 다른 임계값을 계산하여 적용합니다. 이를 통해 명암 차이가 고르지 않은 이미지에서도 효과적으로 객체와 배경을 분리할 수 있습니다. OpenCV에서는 평균값을 이용하는 cv2.ADAPTIVE_THRESH_MEAN_C와 가우시안 가중치를 적용하는 cv2.ADAPTIVE_THRESH_GAUSSIAN_C 두 가지 방식을 제공하며, 블록 크기(blockSize)와 상수 값(C)을 조절하여 최적의 결과를 얻을 수 있습니다.
'''

import cv2
import numpy as np

img = cv2.imread('./images/sudoku.jpg', cv2.IMREAD_GRAYSCALE)

# 전역 자동 이진화
a, dst1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 지역 자동 이진화
dst2 = np.zeros(img.shape, np.uint8)
print(img.shape)
bw = img.shape[1] // 4
bh = img.shape[0] // 4

for y in range(4):
    for x in range(4):
        img_ = img[y*bh: (y+1)*bh, x*bw: (x+1)*bw]
        dst_ = dst2[y*bh: (y+1)*bh, x*bw: (x+1)*bw]
        cv2.threshold(img_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)
        # dst_에 앞에 있는 cv2.THRESH_OTSU 넣어줌

# 적응형 이진화
# ADAPTIVE_THRESH_MEAN_C: 해당 픽셀 주변의 평균값을 기준으로 임계값 설정
# 9: 이웃 블록 크기. 현재 픽셀 주변에서 얼마만큼의 영역을 고려할지 설정. 클수록 더 넓은 영역을 평균 -> 조명에 덜 민감하지만 부드러움
# 5: 임계값 보정 상수, 평균 또는 가중 평균에서 얼마나 빼줄지 결정. 값이 클수록 픽셀이 어두워야 흰색이 됨(임계값을 낮추거나 높이기 위한 튜닝용 파라미터)
dst3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)


# ADAPTIVE_THRESH_GAUSSIAN_C: 주변 픽셀에 가중치를 곱한 평균값으로 임계값 설정
# 조명이 불균일한 이미지에서 효과적, 부드러운 결과
dst4 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 5)



cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)
cv2.waitKey()