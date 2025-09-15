'''
5. 영상의 필터링 연산
영상의 필터링 연산(Image Filtering Operation) 은 영상의 특성을 강조하거나 잡음을 제거하기 위해 커널(필터)을 활용하여 픽셀 값을 변환하는 과정입니다. OpenCV에서는 필터링을 통해 노이즈 제거, 엣지 검출, 블러 효과, 샤프닝 등의 처리를 수행할 수 있습니다. 대표적인 필터링 기법으로는 평균 블러링(Averaging), 가우시안 블러링(Gaussian Blur), 미디언 블러링(Median Blur) 등이 있으며, cv2.blur(), cv2.GaussianBlur(), cv2.medianBlur() 함수를 통해 적용할 수 있습니다. 또한, 고급 필터링 기법으로 소벨 필터(Sobel Filter), 라플라시안 필터(Laplacian Filter) 와 같은 엣지 검출 필터도 제공되며, cv2.Sobel() 및 cv2.Laplacian()을 사용하여 적용할 수 있습니다. 필터링 연산은 영상 내 중요한 특징을 강조하거나 불필요한 정보를 제거하는 데 활용되며, 영상 분석 및 전처리에 필수적인 기법입니다.
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/dog.bmp')
# img = cv2.imread('./images/noise.bmp')
# img = cv2.imread('./images/gaussian_noise.jpg')
dst1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dst2 = cv2.blur(img, (7, 7))

# GaussianBlur
# 픽셀 주변 값들을 가우시안 분포에 따라 가중 평균에서 흐리게 만듦
# 커널 크기가 클수록 넓은 범위를 흐리게 함
# 전체적으로 흐림 처리만 하고 싶을 때
dst3 = cv2.GaussianBlur(img, (0, 0), 2)

# 픽셀 주변의 값 중에서 중간값을 선택해서 새로운 픽셀 값으로 바꾸는 필터
# 이미지의 각 픽셀을 기준으로 주변 픽셀을 확인한 후 그 중에서 가장 중간값(순서대로 정렬)을 가져와서 그 픽셀을 새로운 값으로 바꿔 블러처리 함
dst4 = cv2.medianBlur(img, 7)

# 양방향 필터(bilateralFilter)
# 엣지(윤곽선) 보전하면서 부드럽게 처리할 수 있는 필터
# 공간 정보 + 픽셀 색상 정보를 함께 고려
# 색상 거리 시그마, 공간 거리 시그마
# 노이즈를 줄이고, 윤곽선을 유지하고 싶을 때
dst5 = cv2.bilateralFilter(img, 12, 100, 100)
# Canny 엣지 검출
# 엣지를 찾기 위한 임계값을 자동으로 조절하여 엣지를 찾아주는 알고리즘
# lower threshold: 약한 엣지를 설정
# upper threshold: 강한 엣지를 설정
med_val = np.median(img)
lower = int(max(0, 0.7*med_val))
upper = int(min(255, 1.3*med_val))
print(lower)
print(upper)
dst6 = cv2.GaussianBlur(img, (3, 3), 0)
dst6 = cv2.Canny(dst6, lower, upper, 3)
cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)
cv2.imshow('dst5', dst5)
cv2.imshow('dst6', dst6)
plt.figure(figsize=(10, 5))
for i, k in enumerate([5, 7, 9]):
    # k*k 크기 커널 생성: 예) k=5 1/25로 채워진 5*5 행렬
    kernel = np.ones((k, k)) / k ** 2
    # dst1: 영상, -1: 출력 이미지의 채널을 동일하게,
    filtering = cv2.filter2D(dst1, -1, kernel)
    plt.subplot(1, 3, i+1)
    plt.imshow(filtering)
    plt.title('kernel size: {}'.format(k))
    plt.axis('off')
plt.show()
cv2.waitKey()





