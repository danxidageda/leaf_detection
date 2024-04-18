from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

def create_pdf_from_images(image_paths, output_pdf):
    # 创建一个 PDF 文件
    c = canvas.Canvas(output_pdf, pagesize=letter)

    # 定义每个图像的宽度和高度
    img_width, img_height = letter

    # 逐个添加图像到 PDF
    for i, image_path in enumerate(image_paths):
        # 添加页面
        if i != 0:
            c.showPage()

        # 在 PDF 页面上添加图像
        c.drawImage(image_path, 0, 0, width=img_width, height=img_height)

    # 保存 PDF 文件
    c.save()
    print(f"PDF 文件 '{output_pdf}' 已创建成功。")


if __name__ == "__main__":
    # 定义要转换的图像文件路径和输出 PDF 文件路径
    image_paths = [r"C:\Users\Administrator\Desktop\复试简历\1.png", r"C:\Users\Administrator\Desktop\复试简历\2.png"]
    output_pdf = "output.pdf"

    # 调用函数生成 PDF
    create_pdf_from_images(image_paths, output_pdf)
