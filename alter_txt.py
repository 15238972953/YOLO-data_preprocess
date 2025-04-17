import os

def adjust_labels(input_folder, output_folder, padding_top, original_height, new_height):
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            # 构建完整的文件路径
            input_path = os.path.join(input_folder, filename)
            
            # 读取标签文件
            with open(input_path, 'r') as file:
                lines = file.readlines()
            
            # 处理每一行标签
            adjusted_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) < 5:
                    print(f"警告: 文件 {filename} 中的行 '{line.strip()}' 格式不正确，已跳过")
                    continue
                
                class_id = parts[0]
                cx, cy, w, h = map(float, parts[1:])
                
                # 将比例值转换为像素值
                cy_pixel = cy * original_height
                h_pixel = h * original_height
                
                # 调整中心点坐标
                cy_pixel += padding_top
                
                # 将像素值转换回比例值
                cy_adjusted = cy_pixel / new_height
                h_adjusted = h_pixel / new_height
                
                # 重新构建标签行
                adjusted_line = f"{class_id} {cx} {cy_adjusted} {w} {h_adjusted}\n"
                adjusted_lines.append(adjusted_line)
            
            # 构建输出路径
            output_path = os.path.join(output_folder, filename)
            
            # 保存调整后的标签文件
            with open(output_path, 'w') as file:
                file.writelines(adjusted_lines)
            print(f"标签文件已调整并保存: {output_path}")

# 示例用法
input_folder = 'flowerdata\\val\\labels'
output_folder = 'flower_data\\val\\labels'
original_height = 480
new_height = 640
padding_top = (new_height - original_height) // 2  # 计算顶部填充的高度
adjust_labels(input_folder, output_folder, padding_top, original_height, new_height)