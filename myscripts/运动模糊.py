
import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_motion_blur(image, kernel_size=15, angle=0):
    # 生成运动模糊卷积核
    kernel = np.zeros((kernel_size, kernel_size), dtype=np.float32)

    # 计算卷积核中心位置
    center = (kernel_size - 1) / 2

    # 计算运动模糊方向上的起点和终点坐标
    if angle == 0:  # 水平方向
        start = (int(center - kernel_size / 2), int(center))
        end = (int(center + kernel_size / 2), int(center))
    elif angle == 90:  # 垂直方向
        start = (int(center), int(center - kernel_size / 2))
        end = (int(center), int(center + kernel_size / 2))
    else:  # 其他角度
        theta = np.radians(angle)
        x = center * np.cos(theta)
        y = center * np.sin(theta)
        start = (int(center - x), int(center - y))
        end = (int(center + x), int(center + y))

    # 设置卷积核对应线段的值
    cv2.line(kernel, start, end, 1.0, thickness=1)

    # 归一化卷积核
    kernel /= np.sum(kernel)

    # 应用运动模糊
    blurred_image = cv2.filter2D(image, -1, kernel)

    return blurred_image

# 读取原始图像
image = cv2.imread('../test/data004.jpeg')

# 应用水平方向和垂直方向的运动模糊
blurred_image_horizontal = apply_motion_blur(image, kernel_size=60, angle=0)
blurred_image_vertical = apply_motion_blur(image, kernel_size=60, angle=90)

# 创建子图显示对比图
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 显示原始图像
axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0].set_title('Original Image')
axes[0].axis('off')

# 显示水平和垂直运动模糊后的图像
axes[1].imshow(cv2.cvtColor(blurred_image_horizontal, cv2.COLOR_BGR2RGB))
axes[1].set_title('Horizontal Motion Blur')
axes[1].axis('off')

axes[2].imshow(cv2.cvtColor(blurred_image_vertical, cv2.COLOR_BGR2RGB))
axes[2].set_title('Vertical Motion Blur')
axes[2].axis('off')

# 调整子图间距
plt.tight_layout()

# 保存对比图像到本地文件
plt.savefig('motion_blur_comparison.png')

# 显示对比图
plt.show()
