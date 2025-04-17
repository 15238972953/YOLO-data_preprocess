import os
import torch
from torchvision import transforms
from PIL import Image
import random
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 定义增广方法
transform_brightness_contrast = transforms.Compose([
    transforms.ColorJitter(brightness=(0.5, 1.5), contrast=(0.5, 1.5)),
    transforms.ToTensor()
])

transform_saturation_hue = transforms.Compose([
    transforms.ColorJitter(saturation=(0.5, 1.5), hue=(-0.1, 0.1)),
    transforms.ToTensor()
])

transform_gaussian_blur = transforms.Compose([
    transforms.GaussianBlur(kernel_size=3, sigma=(0.1, 2.0)),
    transforms.ToTensor()
])

def add_random_noise(image):
    noise = np.random.normal(0, 0.1, image.size())
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 1)
    return noisy_image

transform_random_noise = transforms.Compose([
    transforms.ToTensor(),
    transforms.Lambda(add_random_noise)
])

# 定义增广方法列表及其名称
transforms_list = [
    (transform_brightness_contrast, "Brightness and Contrast"),
    (transform_saturation_hue, "Saturation and Hue"),
    (transform_gaussian_blur, "Gaussian Blur"),
    (transform_random_noise, "Random Noise")
]

def apply_single_augment(image, transform, name):
    # 应用单个增广方法
    augmented_image = transform(image)
    return augmented_image, name

def augment_and_save_images(image_folder, label_folder):
    # 获取文件夹中的所有图片文件
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]

    for image_file in image_files:
        # 提取图片序号
        base_name, ext = os.path.splitext(image_file)
        try:
            seq_number = int(base_name.split('_')[-1])
        except ValueError:
            print(f"无法解析图片序号: {image_file}")
            continue

        # 将图片序号+1之后再乘以3
        new_seq_number = (seq_number + 1) * 3
        new_image_file = f"{base_name}_{new_seq_number}{ext}"
        new_image_path = os.path.join(image_folder, new_image_file)

        # 加载原始图像
        image_path = os.path.join(image_folder, image_file)
        image = Image.open(image_path)

        # 随机选择两个增广方法
        selected_transforms = random.sample(transforms_list, 2)

        # 对原始图像分别应用两个增广方法
        augmented_image1, name1 = apply_single_augment(image, selected_transforms[0][0], selected_transforms[0][1])
        augmented_image2, name2 = apply_single_augment(image, selected_transforms[1][0], selected_transforms[1][1])

        # 将增广后的图像转换回PIL图像
        augmented_image1_pil = transforms.ToPILImage()(augmented_image1)
        augmented_image2_pil = transforms.ToPILImage()(augmented_image2)

        # 保存增广后的图像
        augmented_image1_file = f"{base_name}_{new_seq_number-2}{ext}"
        augmented_image2_file = f"{base_name}_{new_seq_number-1}{ext}"
        augmented_image1_path = os.path.join(image_folder, augmented_image1_file)
        augmented_image2_path = os.path.join(image_folder, augmented_image2_file)
        augmented_image1_pil.save(augmented_image1_path)
        augmented_image2_pil.save(augmented_image2_path)

        # 更新对应的标签文件
        label_file = f"{base_name}.txt"
        label_path = os.path.join(label_folder, label_file)
        if os.path.exists(label_path):
            with open(label_path, 'r') as f:
                label_content = f.read()

            augmented_label1_file = f"{base_name}_{new_seq_number-2}.txt"
            augmented_label2_file = f"{base_name}_{new_seq_number-1}.txt"
            augmented_label1_path = os.path.join(label_folder, augmented_label1_file)
            augmented_label2_path = os.path.join(label_folder, augmented_label2_file)

            with open(augmented_label1_path, 'w') as f:
                f.write(label_content)

            with open(augmented_label2_path, 'w') as f:
                f.write(label_content)

        print(f"Processed {image_file} and saved augmented images and labels.")

# 指定输入文件夹
image_folder = "D:\\研究生\\搬花机器人\\software\\视觉\YOLOv11\\dataset_20241122_172954_yolo\\dataset\\test\\images"
label_folder = "D:\\研究生\\搬花机器人\\software\\视觉\YOLOv11\\dataset_20241122_172954_yolo\\dataset\\test\\labels"

# 对文件夹中的所有图片进行增广并保存
augment_and_save_images(image_folder, label_folder)