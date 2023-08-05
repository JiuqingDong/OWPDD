import os
import random
import shutil

def split_dataset(dataset_dir, train_dir, val_dir, test_dir, split_ratio=(0.6, 0.2, 0.2)):
    # 创建保存划分后数据集的目录
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # 获取数据集中的所有文件
    file_list = os.listdir(dataset_dir)
    random.shuffle(file_list)

    # 计算划分后的样本数量
    total_samples = len(file_list)
    train_samples = int(total_samples * split_ratio[0])
    val_samples = int(total_samples * split_ratio[1])
    test_samples = total_samples - train_samples - val_samples

    # 复制文件到相应的目录
    for i, file_name in enumerate(file_list):
        file_path = os.path.join(dataset_dir, file_name)
        if i < train_samples:
            shutil.copy(file_path, os.path.join(train_dir, file_name))
        elif i < train_samples + val_samples:
            shutil.copy(file_path, os.path.join(val_dir, file_name))
        else:
            shutil.copy(file_path, os.path.join(test_dir, file_name))

# 调用函数进行数据集划分
dataset_dir = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/Annotations'
train_dir = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/train'
val_dir = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/val'
test_dir = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/test'
split_ratio = (0.6, 0.2, 0.2)
split_dataset(dataset_dir, train_dir, val_dir, test_dir, split_ratio)
