import os
import xml.etree.ElementTree as ET

def convert_yolo_to_xml(yolo_file, image_width, image_height, classes):
    root = ET.Element("annotation")

    folder = ET.SubElement(root, "folder")
    folder.text = os.path.dirname(yolo_file)

    filename = ET.SubElement(root, "filename")
    filename.text = os.path.basename(yolo_file).split('.')[0] + ".jpg"

    size = ET.SubElement(root, "size")
    width = ET.SubElement(size, "width")
    width.text = str(image_width)
    height = ET.SubElement(size, "height")
    height.text = str(image_height)

    with open(yolo_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split()
            class_index = int(parts[0])
            x_center = float(parts[1])
            y_center = float(parts[2])
            w = float(parts[3])
            h = float(parts[4])

            object_elem = ET.SubElement(root, "object")
            name = ET.SubElement(object_elem, "name")
            name.text = classes[class_index]
            bndbox = ET.SubElement(object_elem, "bndbox")
            xmin = ET.SubElement(bndbox, "xmin")
            xmin.text = str(int((x_center - w / 2) * image_width))
            ymin = ET.SubElement(bndbox, "ymin")
            ymin.text = str(int((y_center - h / 2) * image_height))
            xmax = ET.SubElement(bndbox, "xmax")
            xmax.text = str(int((x_center + w / 2) * image_width))
            ymax = ET.SubElement(bndbox, "ymax")
            ymax.text = str(int((y_center + h / 2) * image_height))

    tree = ET.ElementTree(root)
    return tree

def convert_all_yolo_to_xml(yolo_folder, output_folder, image_width, image_height, classes):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(yolo_folder):
        if filename.endswith(".txt"):
            yolo_file = os.path.join(yolo_folder, filename)
            xml_tree = convert_yolo_to_xml(yolo_file, image_width, image_height, classes)
            xml_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".xml")
            xml_tree.write(xml_file)

# Example usage:
yolo_folder = r"E:\code_for_school\ISAT_with_segment_anything-master\datasets\val\labels"  # Replace with the path to your YOLO annotation folder
output_folder = r"E:\code_for_school\ISAT_with_segment_anything-master\output\val"  # Replace with the path where you want to save the XML files
image_width = 1600  # Replace with the width of your image
image_height = 1600  # Replace with the height of your image
classes = ['curled', 'normal']  # Replace with your class names

convert_all_yolo_to_xml(yolo_folder, output_folder, image_width, image_height, classes)
