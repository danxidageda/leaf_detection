import os
import json
import cv2


def yolo_to_labelme(yolo_label, image_width, image_height, image_filename):
    class_id = yolo_label[0]
    x_center = float(yolo_label[1]) * image_width
    y_center = float(yolo_label[2]) * image_height
    box_width = float(yolo_label[3]) * image_width
    box_height = float(yolo_label[4]) * image_height

    x_min = x_center - (box_width / 2)
    y_min = y_center - (box_height / 2)
    x_max = x_center + (box_width / 2)
    y_max = y_center + (box_height / 2)

    return {
        "label": str(class_id),
        "points": [[x_min, y_min], [x_max, y_max]],
        "group_id": None,
        "description": "",
        "shape_type": "rectangle",
        "flags": {},
        "mask": None
    }


def yolo_to_labelme_file(yolo_file_path, image_folder):
    image_filename = os.path.splitext(os.path.basename(yolo_file_path))[0] + '.jpg'
    image_path = os.path.join(image_folder, image_filename)
    image = cv2.imread(image_path)
    image_height, image_width = image.shape[:2]

    with open(yolo_file_path, 'r') as file:
        lines = file.readlines()

    shapes = []
    for line in lines:
        line = line.strip().split()
        labelme_annotation = yolo_to_labelme(line, image_width, image_height, image_filename)
        shapes.append(labelme_annotation)

    return {
        "version": "5.4.1",
        "flags": {},
        "shapes": shapes,
        "imagePath": image_filename,
        "imageData": None,
        "imageHeight": image_height,
        "imageWidth": image_width
    }


def generate_labelme_json(image_folder, label_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(label_folder):
        if filename.endswith('.txt'):
            yolo_file_path = os.path.join(label_folder, filename)
            labelme_data = yolo_to_labelme_file(yolo_file_path, image_folder)
            output_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.json')
            with open(output_file_path, 'w') as output_file:
                json.dump(labelme_data, output_file, indent=2)


# Example usage:
image_folder = r'E:\code_for_school\ISAT_with_segment_anything-master\output\newtest'
label_folder = r'E:\code_for_school\ISAT_with_segment_anything-master\output\newtest'
output_folder = r'E:\code_for_school\ISAT_with_segment_anything-master\output\labelme'
generate_labelme_json(image_folder, label_folder, output_folder)
