import json
import os
def convert_to_rectangle(json_data):
    converted_data = {
        "version": "5.4.1",
        "flags": {},
        "shapes": [],
        "imagePath": json_data["info"]["name"],
        "imageData": None,
        "imageHeight": json_data["info"]["height"],
        "imageWidth": json_data["info"]["width"]
    }
    for obj in json_data["objects"]:
        segmentation = obj["segmentation"]
        # 计算x和y的最小最大值
        min_x = min(point[0] for point in segmentation)
        max_x = max(point[0] for point in segmentation)
        min_y = min(point[1] for point in segmentation)
        max_y = max(point[1] for point in segmentation)
        # 生成矩形标签
        rect_label = {
            "label": obj["category"],
            "points": [
                [min_x, min_y],
                [max_x, max_y]
            ],
            "group_id": None,
            "shape_type": "rectangle",
            "flags": {},
            "description": "",
            "mask": None
        }
        converted_data["shapes"].append(rect_label)
    return converted_data





def get_json_filenames(folder_path):
    json_files = []
    # 检查文件夹路径是否存在
    if not os.path.exists(folder_path):
        print("指定的文件夹路径不存在。")
        return json_files
    # 遍历文件夹中的所有文件
    for file_name in os.listdir(folder_path):
        # 检查文件是否为JSON文件
        if file_name.endswith('.json'):
            json_files.append(file_name)

    return json_files


# 指定文件夹路径
folder_path = 'E:/code_for_school/biyesheji/test/images/'

# 获取JSON文件列表
json_filenames = get_json_filenames(folder_path)
for json_filename in json_filenames:
    path = folder_path + json_filename
    with open(path, "r") as file:
        polygon_json_data = json.load(file)

    # 转换为矩形标签
    rectangle_json_data = convert_to_rectangle(polygon_json_data)

    # 写入到新的JSON文件
    outputpath = 'E:/code_for_school/biyesheji/test/jsonlabels/' + json_filename
    with open(outputpath, "w") as file:
        json.dump(rectangle_json_data, file, indent=4)

