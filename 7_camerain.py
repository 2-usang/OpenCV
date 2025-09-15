import cv2
import sys

cap = cv2.VideoCapture(0)      # 0 -> 연결되어있는 카메라의 인덱스
if not cap.isOpened():
    print('카메라를 열 수 없음')
    sys.exit()

print('카메라 연결 성공')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print(width)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(height)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

cap.release()