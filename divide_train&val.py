import os, random, shutil

def moveimg(fileDir, tarDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    filenumber = len(pathDir)
    rate = 0.2  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    print(sample)
    for name in sample:
        src_path = os.path.join(fileDir, name)
        dst_path = os.path.join(tarDir, name)
        shutil.move(src_path, dst_path)
    return

def movelabel(file_list, file_label_train, file_label_val):
    for i in file_list:
        if i.endswith('.jpg'):
            label_filename = i[:-4] + '.txt'  # 可以改成xml文件将’.txt‘改成'.xml'就可以了
            src_label_path = os.path.join(file_label_train, label_filename)
            dst_label_path = os.path.join(file_label_val, label_filename)
            if os.path.exists(src_label_path):
                shutil.move(src_label_path, dst_label_path)
                print(f"{i} 处理成功！")

if __name__ == '__main__':
    fileDir = r"train\\images"  # 源图片文件夹路径
    tarDir = r"val\\images"  # 图片移动到新的文件夹路径
    moveimg(fileDir, tarDir)
    
    file_list = os.listdir(tarDir)
    file_label_train = r"train\\labels"  # 源图片标签路径
    file_label_val = r"val\\labels"  # 标签移动到新的文件路径
    movelabel(file_list, file_label_train, file_label_val)