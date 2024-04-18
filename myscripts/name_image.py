
import os

# 获取当前工作目录
current_directory = os.getcwd()

# 指定存储图片的文件夹路径
folder_path = "E:/code_for_school/biyesheji/data/"

# 获取文件夹中所有的文件名
file_names = os.listdir(folder_path)

# 初始化计数器
counter = 1

# 计算填充零所需的宽度
max_count = len(str(len(file_names)))

# 遍历文件夹中的所有文件
for file_name in file_names:
    # 检查文件是否是图片文件（假设为.jpg格式）
    if file_name.endswith('.jpeg'):
        # 构造新的文件名
        new_file_name = "data"+str(counter).zfill(max_count) + '.jpeg'
        # 构造旧的文件路径
        old_file_path = os.path.join(folder_path, file_name)
        # 构造新的文件路径
        new_file_path = os.path.join(folder_path, new_file_name)
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        # 增加计数器
        counter += 1
