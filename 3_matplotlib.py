import cv2
import matplotlib.pyplot as plt

img_gray = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('./images/dog.bmp', cv2.IMREAD_COLOR)
img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.axis('off')
plt.imshow(img_gray, cmap='gray')

plt.subplot(122)
plt.axis('off')
plt.imshow(img_color)
plt.show()

# cv2는 BGR로 읽고 BGR로 보여줌
# plt는 RGB로 보여줌