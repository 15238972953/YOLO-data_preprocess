# YOLO-preprocess（yolo数据集的准备）

## 1、数据标注

ai标注工具：https://trexlabel.com/?source=bl

非常适合多目标标注，一张图片上只需要标注一个目标，其他目标可以自动标注；

标注完成后，直接导出txt格式；

## 2、sort.py

用于将图片数据集和标签文件重命名，这步可以在数据标注前进行；

## 3、extend_square.py

将640x480的图片通过增加黑边变为640x640;

## 4、alter_txt.py

在步骤3后，要对应的修改标注文件中的数据；

## 4、Image_Augmentation.py

图形增广，扩充数据集；

## 5、divide_train&val.py

数据集划分；