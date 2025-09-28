import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/airplane.bmp')
dst1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dst2 = cv2.blur(img, (7, 7))
dst3 = cv2.GaussianBlur(img, (0,0), 2)

# 픽셀 주변의 값 중에서 중간값을 선택해서 새로운 픽셀 값으로 바꾸는 필터
# 이미지의 각 픽셀을 기준으로 주변 픽셀을 확인한 후 그 중에서 가장 중간값
# (순서대로 정렬)을 가져와서 그 픽셀을 새로운 값으로 바꿔 블러처리 함
dst4 = cv2.medianBlur(img, 7)

# 양방향 필터(bilateralFilter)
# 엣지(윤곽선) 보전하면서 부드럽게 처리할 수 있는 필터
# 공간 정보 + 픽셀 색상 정보를 함께 고려
# 색상 거리 시그마, 공간 거리 시그마
# 노이즈를 줄이고, 운곽선을 유지하고 싶을 때
dst5 = cv2.bilateralFilter(img, 12, 100, 100)

cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)

plt.figure(figsize=(10, 5))
for i, k in enumerate([5, 7, 9]):
    kernel = np.ones((k, k)) / k ** 2
    # dst1 : 영상, -1: 출력이미지의 채널을 동일하게
    filtering = cv2.filter2D(dst1, -1, kernel)
    plt.subplot(1, 3, i+1)
    plt.imshow(filtering)
    plt.title('kernel size: {}'.format(k))
    plt.axis('off')
    
plt.show()
cv2.waitKey()