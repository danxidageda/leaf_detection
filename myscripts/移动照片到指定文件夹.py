import os
import shutil

def copy_photos_from_labels(json_folder, photo_folder, destination_folder):
    # 遍历JSON标签文件夹
    for json_file in os.listdir(json_folder):
        if not json_file.endswith('.txt'):
            continue

        json_path = os.path.join(json_folder, json_file)

        # 获取JSON文件的名称
        json_name = os.path.splitext(json_file)[0]

        # 构建照片文件名
        photo_file = json_name + '.png' # 假设照片文件为jpg格式

        # 检查照片文件是否存在
        photo_path = os.path.join(photo_folder, photo_file)
        if os.path.exists(photo_path):
            # 构建目标文件路径
            destination_path = os.path.join(destination_folder, photo_file)

            # 复制照片文件至目标文件夹
            shutil.copyfile(photo_path, destination_path)

            print(f'已复制照片文件: {photo_file}')
        else:
            print(f'未找到照片文件: {photo_file}')


json_folder_path = r'E:\code_for_school\leaf_detection\ultralytics-main\datasets\bigdata\train\labels'
photo_folder_path = r'E:\code_for_school\leaf_detection\ultralytics-main\datasets\bigdata\train\yimages'
destination_folder_path = r'E:\code_for_school\leaf_detection\ultralytics-main\datasets\bigdata\train\images'

# 调用函数复制照片
copy_photos_from_labels(json_folder_path, photo_folder_path, destination_folder_path)

