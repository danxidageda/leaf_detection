# 展示输入图片
from PIL import Image
# 图像地址：https://github.com/obss/sahi/tree/main/demo/demo_data
image_path = "E:/code_for_school/biyesheji/labelme/images/data003.jpeg"
img = Image.open(image_path).convert('RGB')
img
