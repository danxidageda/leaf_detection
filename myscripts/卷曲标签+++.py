import os
import shutil

# 定义文件夹路径
images_folder = r"E:\code_for_school\leaf_detection\ultralytics-main\datasets\mydata\train\images"
labels_folder = r"E:\code_for_school\leaf_detection\ultralytics-main\datasets\mydata\train\labels"
output_images_folder = r"E:\code_for_school\leaf_detection\ultralytics-main\datasets\mydata\output\images"
output_labels_folder = r"E:\code_for_school\leaf_detection\ultralytics-main\datasets\mydata\output\labels"
suffix = "_augmented"  # 添加的特殊后缀

# 确保输出文件夹存在，如果不存在则创建
os.makedirs(output_images_folder, exist_ok=True)
os.makedirs(output_labels_folder, exist_ok=True)

# 遍历标签文件夹中的所有文件
for label_file in os.listdir(labels_folder):
    if label_file.endswith(".txt"):
        with open(os.path.join(labels_folder, label_file), 'r') as f:
            lines = f.readlines()
            new_lines = []
            # 遍历标签文件中的每一行
            for line in lines:
                # 解析标签文件中的类别信息
                class_id, x_center, y_center, width, height = line.strip().split()
                class_id = int(class_id)
                # 如果类别为0，则保留该标签的信息
                if class_id == 0:
                    new_lines.append(line)
            # 如果存在类别为0的标签，则复制对应的图片和标签文件到输出文件夹中
            if new_lines:
                # 查找与标签文件对应的图片文件（支持jpg、png和jpeg格式）
                image_file = os.path.splitext(label_file)[0]
                for image_extension in ['.jpg', '.png', '.jpeg']:
                    if os.path.exists(os.path.join(images_folder, image_file + image_extension)):
                        output_image_file = image_file + suffix + image_extension
                        shutil.copy(os.path.join(images_folder, image_file + image_extension),
                                    os.path.join(output_images_folder, output_image_file))
                        break
                # 复制标签文件，并添加后缀
                output_label_file = os.path.splitext(label_file)[0] + suffix + ".txt"
                with open(os.path.join(output_labels_folder, output_label_file), 'w') as new_f:
                    for line in new_lines:
                        new_f.write(line)
