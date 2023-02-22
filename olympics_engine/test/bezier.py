import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((105, 105))  # 创建一个105x105的画布


def draw(x, y):
    # 平移原点
    x += int(img.shape[0] / 2)
    y += int(img.shape[1] / 2)
    #
    img[-y, x] = 1


print("画布长度为100*100，请输入圆的半径:")
r = int(input())  # 输入圆的半径,单位：像素

d = 1 - r
x = 0
y = r
while (x <= y):  # 根据对称性画出其他七个点
    draw(x, y)
    draw(-x, y)
    draw(x, -y)
    draw(-x, -y)
    draw(y, x)
    draw(y, -x)
    draw(-y, x)
    draw(-y, -x)

    if d <= 0:  # 更新d的值
        d = d + 2 * x + 3
        (x, y) = (x + 1, y)
    else:
        d = d + 2 * (x - y) + 5
        (x, y) = (x + 1, y - 1)
# 绘制图片
plt.imshow(img)
plt.show()
