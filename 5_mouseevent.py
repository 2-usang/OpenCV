import cv2
import numpy as np

oldx = oldy = 0

def on_mouse(event, x, y, flags, param):        # flags : 마우스가 눌렸는지 여부 
    global oldx, oldy
    # print(event, 'x: ',x, 'y:', y, 'flags:', flags)
    if event == cv2.EVENT_LBUTTONDOWN:
        print('왼쪽 버튼이 눌렸어요')
        oldx, oldy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        print('왼쪽 버튼이 떼졌어요')
    elif event == cv2.EVENT_MOUSEMOVE:
        print('마우스가 이동하고 있어요')
        if flags:
            print('드레그중이에요')
            cv2.line(img, (oldx, oldy), (x, y), (255, 51, 255), 3)
            cv2.imshow('img', img)
            oldx, oldy = x, y
        

img = np.ones((500, 500, 3), dtype=np.uint8) * 255

cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 3)
cv2.rectangle(img, (300, 200, 150, 100), (0, 255, 0), -1)   # -1은 사각형 칠해줌
cv2.circle(img, (150, 400), 50, (255, 0,0), 3)  # 위치, 반지름, 색상, 두께
cv2.putText(img, 'car', (50, 200), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0))

cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse)
cv2.waitKey()
