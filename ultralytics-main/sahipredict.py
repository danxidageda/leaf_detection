import os

import PIL.Image

os.getcwd()

from sahi import AutoDetectionModel
from sahi.utils.cv import read_image
from sahi.utils.file import download_from_url
from sahi.predict import get_prediction, get_sliced_prediction, predict
from IPython.display import Image

yolov8_model_path = r"E:\code_for_school\leaf_detection\ultralytics-main\runs\detect\train5\weights\best.pt"


detection_model = AutoDetectionModel.from_pretrained(
    model_type='yolov8',
    # YOLOv8模型的路径
    model_path=yolov8_model_path,
    # YOLOv8模型的路径
    confidence_threshold=0.5,
    # 设备类型。
    # 如果您的计算机配备 NVIDIA GPU，则可以通过将 'device' 标志更改为'cuda:0'来启用 CUDA 加速；否则，将其保留为'cpu'
    device="cuda:0", # or 'cuda:0'
)

result = get_sliced_prediction(
    r"E:\code_for_school\leaf_detection\ultralytics-main\test_images\bigimages\10.jpeg",
    detection_model,
    slice_height = 1500,
    slice_width = 2000,
    overlap_height_ratio = 0,
    overlap_width_ratio = 0
)
result.export_visuals(export_dir="output/")
#
Image("output/prediction_visual.png")
import streamlit as st
from PIL import Image

source_img = st.sidebar.file_uploader(
    label="Choose an image...",
    type=("jpg", "jpeg", "png", 'bmp', 'webp')
)
# 创建一个 PIL Image 对象
# 在 Streamlit 中显示 PIL Image 对象
st.image(PIL.Image.open(source_img), caption='Uploaded Image', use_column_width=True)
