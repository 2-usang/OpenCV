'''
4. 영상의 변환
영상의 변환(Image Transformation) 이란 영상의 형태, 크기, 밝기, 색상 등을 변경하여 새로운 영상으로 변환하는 과정으로, 컴퓨터 비전에서 다양한 전처리 및 후처리에 활용됩니다. OpenCV에서는 대표적으로 기하학적 변환(Geometric Transformation) 과 강도 변환(Intensity Transformation) 을 제공합니다. 
기하학적 변환에는 확대/축소(Scaling), 회전(Rotation), 이동(Translation), 투시 변환(Perspective Transform) 등이 있으며, cv2.warpAffine()과 cv2.getPerspectiveTransform()을 통해 수행할 수 있습니다. 
강도 변환은 픽셀 값의 변화를 조정하는 방법으로 명암 조절, 히스토그램 평활화, 이진화(Thresholding) 등이 있으며, cv2.equalizeHist(), cv2.threshold(), cv2.adaptiveThreshold() 등이 이에 해당합니다.
'''

import cv2
import numpy as np

img = cv2.imread('./images/dog.bmp')

# 어파인 행렬
aff = np.array([
    [1, 0, 150], 
    [0, 1, 100]
    ], dtype=np.float32)

# 어파인 변환
# 이미지의 위치나 모양을 변경하는 선형 변환
dst = cv2.warpAffine(img, aff, (0, 0))  # (0,0) : 원본 이미지 크기를 그대로 전달

# interpolation(보간법) : 픽셀을 어떻게 채울지 결정
# INTER_NEAREST : 최근법 이웃 보간(속도 빠름, 품질 낮음). 가까운 픽셀 값을 그대로 복사. 계단 현상이나 노이즈가 생길 수 있음
# INTER_CUBIC : 4차 보간법, (속도 느림, 품질 좋음), 주변 16개 픽셀을 사용하여 곡선으로 예측, 이미지를 부드럽게 확대/축소
dst2 = cv2.resize(img, (1280, 1024), interpolation=cv2.INTER_NEAREST)
dst3 = cv2.resize(img, (1280, 1024), interpolation=cv2.INTER_CUBIC)

cp = (img.shape[1] / 2, img.shape[0] / 2)
rot = cv2.getRotationMatrix2D(cp, 30, 0.7)      # -> 행렬 생성
# 30 : 각도, 0.7 : 크기(70%)
dst4 = cv2.warpAffine(img, rot, (0, 0))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)
cv2.waitKey()