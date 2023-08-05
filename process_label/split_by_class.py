import os
import shutil
import xml.etree.ElementTree as ET

def organize_files_by_class(voc_dir, output_dir):
    # 创建输出文件夹
    os.makedirs(output_dir, exist_ok=True)

    # 遍历VOC数据集中的每个XML文件
    for root, dirs, files in os.walk(voc_dir):
        for file in files:
            if file.endswith('.xml'):
                xml_file = os.path.join(root, file)
                # 解析XML文件
                tree = ET.parse(xml_file)
                roots = tree.getroot()

                # 查找所有的"object"元素
                objects = roots.findall('object')
                for obj in objects:
                    # 查找"name"元素并获取类别名称
                    name = obj.find('name')
                    class_name = name.text

                    # 创建类别文件夹
                    class_dir = os.path.join(output_dir, class_name)
                    os.makedirs(class_dir, exist_ok=True)

                    # 将标注文件复制到对应的类别文件夹中
                    shutil.copy(xml_file, class_dir)

# 调用函数按类别组织标注文件
voc_dir = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/train'
output_dir = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/All_class'  # 指定输出文件夹路径
organize_files_by_class(voc_dir, output_dir)


def count_subfiles(folder_path):
    count = 0

    # 遍历文件夹中的所有子文件
    for root, dirs, files in os.walk(folder_path):
        count += len(files)  # 计数文件数量
        count += len(dirs)   # 计数文件夹数量

    return count


def count_duplicate_files(folder_path):
    file_count = {}
    duplicate_count = 0

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 获取文件名
            filename = os.path.basename(file)
            # 统计文件名的出现次数
            if filename in file_count:
                file_count[filename] += 1
                if file_count[filename] == 2:
                    duplicate_count += 1
            else:
                file_count[filename] = 1

    return duplicate_count


# 调用函数查询子文件数量
folder_path = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/All_class'  # 指定文件夹路径
subfile_count = count_subfiles(folder_path)
print(f"子文件数量: {subfile_count}")

# 调用函数查询重名文件数量
duplicate_count = count_duplicate_files(folder_path)
print(f"重名文件数量: {duplicate_count}")