# from ultralytics import YOLO
# import torch
# if __name__ == '__main__':
#     # Load a model
#     model = YOLO('yolov8.yaml')  # build a new model from YAML
#     model = YOLO('yolov8m.pt')  # load a pretrained model (recommended for training)
#     model = YOLO('yolov8.yaml').load('yolov8m.pt')  # build from YAML and transfer weights
#
#     # Train the model
#     results = model.train(data='my_configure/mydata.yaml', epochs=300, imgsz=640)
#
#
from ultralytics import YOLO
import torch
if __name__ == '__main__':
    # Load a model
    model = YOLO('my_configure/yolov8s.yaml')  # build a new model from YAML
    model = YOLO('yolov8s.pt')  # load a pretrained model (recommended for training)
    model = YOLO('my_configure/yolov8s.yaml').load('yolov8s.pt')  # build from YAML and transfer weights

    # Train the model
    results = model.train(data='my_configure/mydata.yaml', epochs=50, imgsz=640,patience=40)