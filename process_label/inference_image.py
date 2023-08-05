import os
import shutil

# 定义源文件夹和目标文件夹
src_dir = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/JPEGImages'
dst_dir = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/Inference'

# 读取图片路径列表
with open('/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/ImageSets/Main/all_task_test.txt', 'r') as f:
    image_paths = f.readlines()

from collections import Counter

counts = Counter(image_paths)

# 输出结果
print(counts)

# 拷贝图片到目标文件夹下
for path in image_paths:
    # 去除路径中的换行符
    path = path.strip()
    # 生成源文件和目标文件的路径
    src_path = os.path.join(src_dir, path+".jpg")
    dst_path = os.path.join(dst_dir, path+".jpg")
    # 拷贝文件
    shutil.copyfile(src_path, dst_path)
