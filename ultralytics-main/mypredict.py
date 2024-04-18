
from ultralytics import YOLO

# Load a model
model = YOLO(r'E:\code_for_school\leaf_detection\ultralytics-main\runs\detect\train2\weights\best.pt')  # pretrained YOLOv8n model

# Run batched inference on a list of images
results = model(r'datasets/onlycurleddata/val/images/data823_1696_696_4000_3000.png')  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    result.show()  # display to screen
    result.save(filename='result.jpg')  # save to disk

# from ultralytics import YOLO
#
# # Load a pretrained YOLOv8n model
# model = YOLO(r'E:\code_for_school\leaf_detection\ultralytics-main\runs\detect\train\weights\best.pt')
#
# # Run inference on 'bus.jpg' with arguments
# model.predict(r'E:\code_for_school\leaf_detection\ultralytics-main\test_images\samllimages\1.png', save=True, imgsz=640, conf=0.7)