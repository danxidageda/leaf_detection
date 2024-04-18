# import os
# import cv2
# import numpy as np
#
#
# def add_salt_pepper_noise(image, salt_pepper_prob=0.05):
#     noisy_image = np.copy(image)
#     height, width = image.shape[:2]
#
#     # 添加椒盐噪声
#     salt_pepper = np.random.rand(height, width)
#     noisy_image[salt_pepper < salt_pepper_prob / 2] = 0
#     noisy_image[salt_pepper > 1 - salt_pepper_prob / 2] = 255
#
#     return noisy_image
#
#
# def apply_gaussian_blur(image, kernel_size=(5, 5)):
#     # 高斯模糊
#     blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
#
#     return blurred_image
#
#
#
# def augment_data(image_folder, label_folder, output_folder, salt_pepper_prob=0.05, gaussian_blur_kernel=(5, 5)):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#
#     for filename in os.listdir(image_folder):
#         if filename.endswith((".jpg", ".png")):
#             image_path = os.path.join(image_folder, filename)
#             label_path = os.path.join(label_folder, os.path.splitext(filename)[0] + ".txt")
#
#             # 读取图像
#             image = cv2.imread(image_path)
#             labels = []
#
#             # 读取对应的标签
#             with open(label_path, 'r') as f:
#                 for line in f:
#                     label = [float(x) for x in line.strip().split()]
#                     labels.append(label)
#
#             # 添加椒盐噪声
#             noisy_image_salt_pepper = add_salt_pepper_noise(image, salt_pepper_prob)
#
#             # 保存增强后的图像
#             output_image_salt_pepper_path = os.path.join(output_folder,
#                                                          os.path.splitext(filename)[0] + "_salt_pepper.jpg")
#             cv2.imwrite(output_image_salt_pepper_path, noisy_image_salt_pepper)
#
#             # 保存椒盐噪声对应的标签
#             output_label_salt_pepper_path = os.path.join(output_folder,
#                                                          os.path.splitext(filename)[0] + "_salt_pepper.txt")
#             with open(output_label_salt_pepper_path, 'w') as f_salt_pepper:
#                 for label in labels:
#                     # 将类别标签转换为整数格式
#                     label[0] = int(label[0])
#                     f_salt_pepper.write(' '.join([str(x) for x in label]) + '\n')
#
#             # 高斯模糊
#             blurred_image = apply_gaussian_blur(image, gaussian_blur_kernel)
#             output_image_blurred_path = os.path.join(output_folder, os.path.splitext(filename)[0] + "_blurred.jpg")
#             cv2.imwrite(output_image_blurred_path, blurred_image)
#
#             # 保存高斯模糊对应的标签
#             output_label_blurred_path = os.path.join(output_folder, os.path.splitext(filename)[0] + "_blurred.txt")
#             with open(output_label_blurred_path, 'w') as f_blurred:
#                 for label in labels:
#                     # 将类别标签转换为整数格式
#                     label[0] = int(label[0])
#                     f_blurred.write(' '.join([str(x) for x in label]) + '\n')
#
#
#
# image_folder = r"E:\code_for_school\leaf_detection\ultralytics-main\datasets\onlycurleddata\train\images"
# label_folder = r"E:\code_for_school\leaf_detection\ultralytics-main\datasets\onlycurleddata\train\labels"
# output_folder = r"E:\code_for_school\leaf_detection\ultralytics-main\datasets\onlycurleddata\output"
# salt_pepper_prob = 0.05  # 椒盐噪声概率
# gaussian_blur_kernel = (3, 3)  # 高斯模糊核大小
# augment_data(image_folder, label_folder, output_folder, salt_pepper_prob, gaussian_blur_kernel)
#
#


import os
import cv2
import numpy as np


def apply_gaussian_blur(image, kernel_size=(5, 5)):
    # 高斯模糊
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    return blurred_image


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


def augment_data(image_folder, label_folder, output_folder, gaussian_blur_kernel=(5, 5), motion_blur_params=None):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(image_folder):
        if filename.endswith((".jpg", ".png")):
            image_path = os.path.join(image_folder, filename)
            label_path = os.path.join(label_folder, os.path.splitext(filename)[0] + ".txt")

            # 读取图像
            image = cv2.imread(image_path)
            labels = []

            # 读取对应的标签
            with open(label_path, 'r') as f:
                for line in f:
                    label = [float(x) for x in line.strip().split()]
                    labels.append(label)

            # 高斯模糊
            blurred_image = apply_gaussian_blur(image, gaussian_blur_kernel)
            output_image_blurred_path = os.path.join(output_folder, os.path.splitext(filename)[0] + "_blurred.jpg")
            cv2.imwrite(output_image_blurred_path, blurred_image)

            # 保存高斯模糊对应的标签
            output_label_blurred_path = os.path.join(output_folder, os.path.splitext(filename)[0] + "_blurred.txt")
            with open(output_label_blurred_path, 'w') as f_blurred:
                for label in labels:
                    # 将类别标签转换为整数格式
                    label[0] = int(label[0])
                    f_blurred.write(' '.join([str(x) for x in label]) + '\n')

            # 运动模糊
            if motion_blur_params:
                motion_blur_image = apply_motion_blur(image, **motion_blur_params)
                output_image_motion_blur_path = os.path.join(output_folder,
                                                             os.path.splitext(filename)[0] + "_motion_blur.jpg")
                cv2.imwrite(output_image_motion_blur_path, motion_blur_image)

                # 保存运动模糊对应的标签
                output_label_motion_blur_path = os.path.join(output_folder,
                                                             os.path.splitext(filename)[0] + "_motion_blur.txt")
                with open(output_label_motion_blur_path, 'w') as f_motion_blur:
                    for label in labels:
                        # 将类别标签转换为整数格式
                        label[0] = int(label[0])
                        f_motion_blur.write(' '.join([str(x) for x in label]) + '\n')


image_folder = r"E:\code_for_school\leaf_detection\ultralytics-main\datasets\15002000data\val\images"
label_folder = r"E:\code_for_school\leaf_detection\ultralytics-main\datasets\15002000data\val\labels"
output_folder = r"E:\code_for_school\leaf_detection\ultralytics-main\datasets\15002000data\output"
gaussian_blur_kernel = (3, 3)  # 高斯模糊核大小
motion_blur_params = {'kernel_size': 30, 'angle': 45}  # 运动模糊参数

augment_data(image_folder, label_folder, output_folder, gaussian_blur_kernel, motion_blur_params)


