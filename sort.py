import os

def rename_images_in_folder(folder_path):
    # 获取文件夹中所有文件的列表
    files = os.listdir(folder_path)

    # 过滤出图片文件（假设图片文件扩展名为.jpg、.png、.jpeg）
    image_files = [f for f in files if f.lower().endswith(('.jpg', '.png', '.jpeg','txt'))]

    # 按文件名排序（可选）
    image_files.sort()

    # 重命名图片
    for i, filename in enumerate(image_files):
        old_path = os.path.join(folder_path, filename)
        new_filename = f'flower_{i:05d}.txt'  # 生成新的文件名，数字部分为四位数
        new_path = os.path.join(folder_path, new_filename)

        # 重命名文件
        os.rename(old_path, new_path)
        print(f"重命名: {old_path} -> {new_path}")


# 指定文件夹路径
folder_path = 'labels'

# 调用函数
rename_images_in_folder(folder_path)
