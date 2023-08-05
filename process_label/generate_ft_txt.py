import os
import random

def select_random_files(folder_path, num_files):
    file_list = []

    # 遍历文件夹中的子文件夹
    for root, dirs, files in os.walk(folder_path):
        # 在每个子文件夹中随机选择指定数量的文件
        selected_files = random.sample(files, min(num_files, len(files)))
        # 构造完整的文件路径并添加到列表中
        file_list.extend([os.path.join(root, file) for file in selected_files])

    return file_list

def save_file_list_to_txt(file_list, output_file):
    with open(output_file, 'w') as f:
        for file_path in file_list:
            # 获取文件名
            file_name = os.path.basename(file_path)
            file_name = file_name.replace('.xml', '')
            # 写入文件名到txt文档
            f.write(file_name + '\n')

# 调用函数随机选择文件并保存到txt文档
for taskID in ['t1','t2','t3','t4']:
    folder_path = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/All_class/{}'.format(taskID)  # 指定文件夹路径
    num_files_per_folder = 25  # 每个子文件夹中要选择的文件数量
    output_file = '{}_ft.txt'.format(taskID)  # 指定输出文件名

    file_list = select_random_files(folder_path, num_files_per_folder)
    save_file_list_to_txt(file_list, output_file)
