import os
import xml.etree.ElementTree as ET

def count_instances(voc_dir, class_order, num_instances):
    class_counts = {}

    # 初始化类别计数为0
    for class_name in class_order:
        class_counts[class_name] = 0

    # 初始化已选取实例计数为0
    selected_counts = {}

    # 遍历VOC数据集中的每个XML文件
    for root, dirs, files in os.walk(voc_dir):
        for file in files:
            if file.endswith('.xml'):
                xml_file = os.path.join(root, file)
                # 解析XML文件
                tree = ET.parse(xml_file)
                root = tree.getroot()

                # 查找所有的"object"元素
                objects = root.findall('object')
                for obj in objects:
                    # 查找"name"元素并统计每个类别的实例数
                    name = obj.find('name')
                    class_name = name.text
                    if class_name in class_order and class_counts[class_name] < num_instances:
                        class_counts[class_name] += 1
                        if class_name not in selected_counts:
                            selected_counts[class_name] = 1
                        else:
                            selected_counts[class_name] += 1

    return selected_counts

# 调用函数选取指定数量的实例
voc_dir = 'path/to/your/voc_dataset'
class_order = ['class1', 'class2', 'class3']  # 按照指定顺序列出类别名称
num_instances = 50  # 指定每个类别选取的实例数量
selected_counts = count_instances(voc_dir, class_order, num_instances)

# 打印每个类别选取的实例数量
for class_name, count in selected_counts.items():
    print(f'{class_name}: {count} instances selected')
