import cv2
import numpy as np

img_gray = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)

print('img_gray type: ', type(img_gray))
print('img_gray shape: ', img_gray.shape) # 세로, 가로 (364, 548)
# opencv에서는 세로, 가로 순서
print('img_gray dtype: ', img_gray.dtype)
# uint8 -> 밝기 정보를 표현하기 위한 데이터 타입

img_color = cv2.imread('./images/dog.bmp')

print('img_gray type: ', type(img_color))
print('img_gray shape: ', img_color.shape)      # (364, 548, 3)
print('img_gray dtype: ', img_color.dtype)

h, w = img_color.shape[:2]
print(f'이미지 사이즈 : {w} * {h}')

if len(img_color.shape) == 3:
    print('컬러영상')
elif len(img_color.shape) == 2:
    print('그레이 스케일')

img1 = np.zeros((240, 320, 3), dtype=np.uint8)
img2 = np.empty((240, 320), dtype=np.uint8)
img3 = np.ones((240, 320), dtype=np.uint8)*120
img4 = np.full((240, 320, 3), (255, 102, 255), dtype=np.uint8)

img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
h, w = img2.shape[:2]
# for x in range(h):
#     for y in range(w):
#         img2[x,y] = (255, 102, 255)

img2[:, :] = (255, 102, 255)


print(img4)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.imshow('img_color', img_color)

while True:
    keyvalue = cv2.waitKey()
    print(keyvalue)
    if keyvalue == ord('i') or keyvalue == ord('I'):    # ord는 아스키코드 변환
        img_color = ~img_color
        cv2.imshow('img_color', img_color)
    elif keyvalue == 27:
        break

cv2.waitKey()

