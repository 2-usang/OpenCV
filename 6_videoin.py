import cv2
import sys

cap = cv2.VideoCapture('./movies/296958_tiny.mp4')      #  동영상 불러들이는 객체가 만들어짐
if not cap.isOpened():
    print('동영상을 불러올 수 없음')
    sys.exit()

print('동영상을 불러올 수 있음')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print(width)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(height)

frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(frame_count)

fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

# 반복문을 돌리는 속도 때문에 영상 속도가 빠름
while True:
    ret, frame = cap.read()     
    # 프레임을 읽어들이다가 다음 프레임이 없으면 ret가 false가 됨
    # frame에 ndarray 값이 들어옴
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27: # 1000분의 n초 -> 해당 시간만큼 대기
        break

cap.release()   # 메모리 정리