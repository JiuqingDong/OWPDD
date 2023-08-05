import os

def save_file_names_to_txt(folder_path, output_file):
    with open(output_file, 'w') as f:
        # 遍历文件夹中的所有文件
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file = file.replace('.xml', '')
                # 写入文件名到txt文档
                f.write(file + '\n')

# 调用函数保存文件名到txt文档
folder_path = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/val'  # 指定文件夹路径
output_file = 'all_task_val.txt'  # 指定输出文件名
save_file_names_to_txt(folder_path, output_file)


folder_path = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/test'  # 指定文件夹路径
output_file = 'all_task_test.txt'  # 指定输出文件名
save_file_names_to_txt(folder_path, output_file)

