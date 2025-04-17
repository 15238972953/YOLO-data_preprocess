import cv2
import os

def pad_images(input_folder, output_folder):
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        # 构建完整的文件路径
        input_path = os.path.join(input_folder, filename)
        
        # 读取图片
        image = cv2.imread(input_path)
        
        # 检查图片是否成功读取
        if image is None:
            print(f"无法读取图片: {input_path}")
            continue
        
        # 获取图片的高度和宽度
        height, width = image.shape[:2]
        
        # 检查图片尺寸是否为640x480
        if width == 640 and height == 480:
            # 计算需要填充的黑色区域的高度
            new_height = 640
            padding_top = (new_height - height) // 2
            padding_bottom = new_height - height - padding_top
            
            # 填充黑色区域
            padded_image = cv2.copyMakeBorder(image, padding_top, padding_bottom, 0, 0, cv2.BORDER_CONSTANT, value=[0, 0, 0])
            
            # 构建输出路径
            output_path = os.path.join(output_folder, filename)
            
            # 保存填充后的图片
            cv2.imwrite(output_path, padded_image)
            print(f"图片已填充并保存: {output_path}")
        else:
            print(f"跳过图片: {input_path}，尺寸不符合640x480")

# 示例用法
input_folder = 'flowerdata\\test'
output_folder = 'flower_data\\test'
pad_images(input_folder, output_folder)