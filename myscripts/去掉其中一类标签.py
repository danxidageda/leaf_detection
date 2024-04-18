import os

# 定义标签文件夹路径
label_folder = r"E:\code_for_school\leaf_detection\ultralytics-main\datasets\15002000data\train\labels"

# 获取标签文件夹中所有的标签文件
label_files = [file for file in os.listdir(label_folder) if file.endswith('.txt')]

# 定义需要删除的类别
class_to_remove = "1"

# 遍历每个标签文件
for label_file in label_files:
    label_file_path = os.path.join(label_folder, label_file)
    with open(label_file_path, 'r') as f:
        lines = f.readlines()

    # 过滤出不含指定类别的行
    filtered_lines = [line for line in lines if line.strip().split()[0] != class_to_remove]

    # 将过滤后的行重新写入标签文件
    with open(label_file_path, 'w') as f:
        f.writelines(filtered_lines)

print("已完成标签处理。")
