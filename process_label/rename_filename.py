import os

def rename_files(folder_path, start_count):
    count = start_count

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # 构造新的文件名
            new_file_name = f"{count}{os.path.splitext(file_name)[1]}"
            # 构造旧的文件路径和新的文件路径
            old_file_path = os.path.join(root, file_name)
            new_file_path = os.path.join(root, new_file_name)
            print(old_file_path, new_file_path)
            old_file_path_xml = old_file_path.replace('JPEGImages', 'Annotations')
            old_file_path_xml = old_file_path_xml.replace('.jpg', '.xml')
            new_file_path_xml = new_file_path.replace('JPEGImages', 'Annotations')
            new_file_path_xml = new_file_path_xml.replace('.jpg', '.xml')
            print(old_file_path_xml, new_file_path_xml)

            # 重命名文件
            os.rename(old_file_path, new_file_path)
            os.rename(old_file_path_xml, new_file_path_xml)
            count += 1

# 调用函数修改文件名
folder_path = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/JPEGImages'  # 指定文件夹路径
start_count = 10000000  # 起始计数值
rename_files(folder_path, start_count)
