import json
import os


def labelme_to_coco(labelme_json_folder, save_path):
    # 创建 COCO 格式的字典
    coco_data = {
        "info": {},
        "licenses": [],
        "images": [],
        "annotations": [],
        "categories": []
    }

    # 类别名称和 ID 映射
    category_id_map = {}
    category_id = 1

    # 读取 LabelMe 标注文件夹中的每个 JSON 文件
    for filename in os.listdir(labelme_json_folder):
        if filename.endswith('.json'):
            with open(os.path.join(labelme_json_folder, filename), 'r') as f:
                labelme_data = json.load(f)

            # 添加图像信息
            image_info = {
                "id": len(coco_data["images"]) + 1,
                "file_name": labelme_data["imagePath"],
                "width": labelme_data["imageWidth"],
                "height": labelme_data["imageHeight"]
            }
            coco_data["images"].append(image_info)

            # 添加标注信息
            for shape in labelme_data["shapes"]:
                category = shape["label"]
                if category not in category_id_map:
                    category_id_map[category] = category_id
                    category_id += 1

                category_id_label = category_id_map[category]

                bbox_x = min(shape["points"][0][0], shape["points"][1][0])
                bbox_y = min(shape["points"][0][1], shape["points"][1][1])
                bbox_width = abs(shape["points"][0][0] - shape["points"][1][0])
                bbox_height = abs(shape["points"][0][1] - shape["points"][1][1])

                annotation = {
                    "id": len(coco_data["annotations"]) + 1,
                    "image_id": image_info["id"],
                    "category_id": category_id_label,
                    "bbox": [bbox_x, bbox_y, bbox_width, bbox_height],
                    "iscrowd": 0,
                    "area": bbox_width * bbox_height,
                    "ignore": 0
                }
                coco_data["annotations"].append(annotation)

    # 添加类别信息
    for category, category_id in category_id_map.items():
        coco_data["categories"].append({
            "id": category_id,
            "name": category,
            "supercategory": "object"
        })

    # 保存为 JSON 文件
    with open(save_path, 'w') as f:
        json.dump(coco_data, f)


# 使用示例
labelme_json_folder = "E:/code_for_school/biyesheji/test/jsonlabels"
save_path = "coco.json"
labelme_to_coco(labelme_json_folder, save_path)
