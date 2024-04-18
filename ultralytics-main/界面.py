import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

from ultralytics import YOLO

class YOLOInferenceApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('基于无人机遥感图像的荔枝叶卷曲检测')
        self.setGeometry(100, 100, 1920, 1080)  # 设置窗口大小为1920x1080

        # 按钮大小的比例因子
        button_scale_factor = 0.9

        self.lbl_image = QLabel(self)
        self.lbl_image.setGeometry(100, 100, 600, 600)

        self.lbl_result = QLabel(self)
        self.lbl_result.setGeometry(900, 100, 600, 600)

        self.btn_upload_image = QPushButton('上传照片', self)
        self.btn_upload_image.setGeometry(100, 800, int(300 * button_scale_factor), int(100 * button_scale_factor))
        self.btn_upload_image.clicked.connect(self.upload_image)

        self.btn_choose_model = QPushButton('选择模型', self)
        self.btn_choose_model.setGeometry(500, 800, int(300 * button_scale_factor), int(100 * button_scale_factor))
        self.btn_choose_model.clicked.connect(self.choose_model)

        self.btn_run_inference = QPushButton('运行推理', self)
        self.btn_run_inference.setGeometry(900, 800, int(300 * button_scale_factor), int(100 * button_scale_factor))
        self.btn_run_inference.clicked.connect(self.run_yolo_inference)

        self.btn_exit = QPushButton('退出', self)
        self.btn_exit.setGeometry(1300, 800, int(200 * button_scale_factor), int(100 * button_scale_factor))
        self.btn_exit.clicked.connect(self.close)

        # 显示原始照片和推理照片的文本标签
        self.lbl_original_text = QLabel('原始照片', self)
        self.lbl_original_text.setFont(QFont('Arial', 20))
        self.lbl_original_text.setGeometry(100, 50, 200, 30)
        self.lbl_original_text.setAlignment(Qt.AlignCenter)

        self.lbl_inference_text = QLabel('推理照片', self)
        self.lbl_inference_text.setFont(QFont('Arial', 20))
        self.lbl_inference_text.setGeometry(900, 50, 200, 30)
        self.lbl_inference_text.setAlignment(Qt.AlignCenter)

        self.selected_image_label = QLabel(self)
        self.selected_image_label.setGeometry(100, 720, 800, 50)
        self.selected_image_label.setWordWrap(True)  # 自动换行
        self.selected_image_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)  # 左上对齐

        self.selected_model_label = QLabel(self)
        self.selected_model_label.setGeometry(100, 770, 800, 50)
        self.selected_model_label.setWordWrap(True)  # 自动换行
        self.selected_model_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)  # 左上对齐

        self.show()

    def upload_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, '上传照片', '', 'Image Files (*.png *.jpg *.jpeg)', options=options)
        if file_path:
            pixmap = QPixmap(file_path)
            pixmap = pixmap.scaled(600, 600)
            self.lbl_image.setPixmap(pixmap)

            self.image_path = file_path
            self.selected_image_label.setText(f'已选择的照片：{file_path}')


        else:
            QMessageBox.warning(self, '警告', '请选择一个照片！')

    def choose_model(self):
        options = QFileDialog.Options()
        model_path, _ = QFileDialog.getOpenFileName(self, '选择模型', '', 'Model Files (*.pt)', options=options)
        if model_path:
            self.model = YOLO(model_path)
            self.selected_model_label.setText(f'已选择的模型：{model_path}')
        else:
            QMessageBox.warning(self, '警告', '请选择一个模型！')

    def run_yolo_inference(self):
        if hasattr(self, 'model') and hasattr(self, 'image_path'):
            # Clear previous result
            self.lbl_result.clear()

            # Run inference on the selected image
            results = self.model(self.image_path)

            # Display and save the first result
            result = results[0]
            result.show()
            result.save(filename='result.jpg')

            # Display result image
            pixmap = QPixmap('result.jpg')
            pixmap = pixmap.scaled(600, 600)
            self.lbl_result.setPixmap(pixmap)


        else:
            QMessageBox.warning(self, '警告', '请先选择照片和模型！')

def main():
    app = QApplication(sys.argv)
    window = YOLOInferenceApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
