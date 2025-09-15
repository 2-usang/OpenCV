import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./images/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

# 히스토그램 평활화
# 이미지의 전체 밝기 분포를 고르게 퍼뜨려 명암 대비를 향상시키는 기법
dst1 = cv2.equalizeHist(img1)

img2 = cv2.imread('./images/field.bmp')

# YCrCb 색공간
# Y: 밝기(명도), Cr: 빨강 계열 색상 정보, Cb: 파랑 계열 색상 정보
dst2 = cv2.cvtColor(img2, cv2.COLOR_BGR2YCrCb)

'''
ycrcb = cv2.split(dst2)
# print(type(ycrcb))  # <class 'tuple'>
ycrcb = list(ycrcb)
# # print(ycrcb)
ycrcb[0] = cv2.equalizeHist(ycrcb[0])   # Y(명도) 채널만 뽑아서
dst2 = cv2.merge(ycrcb)     # split 한거 다시 합쳐줌
'''

dst2[:, :, 0] = cv2.equalizeHist(dst2[:, :, 0])     # 위 주석 부분과 같은 역할
dst2 = cv2.cvtColor(dst2, cv2.COLOR_YCrCb2BGR)

# img1: 원본 이미지 또는 배열
# None: 출력 배열(None이면 새로 생성)
# 0: 정규화 후 최소값
# 255: 정규화 후 최대값
# cv2.NORM_MINMAX 정규화 방식
dst3 = cv2.normalize(img1, None, 0, 255, cv2.NORM_MINMAX)

hist1 = cv2.calcHist([img1], [0], None, [256], [0, 255])
hist2 = cv2.calcHist([dst1], [0], None, [256], [0, 255])
hist3 = cv2.calcHist([dst3], [0], None, [256], [0, 255])

hists = {'hist1': hist1, 'hist2': hist2, 'hist3': hist3}

cv2.imshow('img1', img1)
cv2.imshow('dst1', dst1)

cv2.imshow('img2', img2)
cv2.imshow('dst2', dst2)

cv2.imshow('dst3', dst3)

plt.figure(figsize=(12, 8))
for i, (k, v) in enumerate(hists.items()):
    plt.subplot(1, 3, i+1)
    plt.title(k)
    plt.plot(v)
plt.show()

cv2.waitKey()