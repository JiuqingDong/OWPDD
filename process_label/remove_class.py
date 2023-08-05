# Alvaro's task.

import xml.etree.ElementTree as ET
from lxml import etree
import os


def get_value(category, xmin, xmax, ymin, ymax):
    category = str(category.text)
    xmin = int(xmin.text)
    xmax = int(xmax.text)
    ymin = int(ymin.text)
    ymax = int(ymax.text)

    return category, xmin, xmax, ymin, ymax


def calculate_ratio(width, height, xmin, xmax, ymin, ymax):
    img = width*height
    instance = (xmax-xmin) * (ymax - ymin)
    ratio = instance/img

    return ratio


def remove_instance(xml_file, target):
    SAVE =True
    target_file = xml_file.replace('Annotations', target)            # 需要修改

    parser = etree.XMLParser(remove_blank_text=True)  #
    root = etree.parse(xml_file, parser)
    tree = etree.ElementTree(root.getroot())

    size = root.find('size')            # 读取图像尺寸信息
    width = int(size.find('width').text)
    height = int(size.find('height').text)
    small = 0

    for object in tree.findall('object'):       # 遍历对象类别与位置信息。
        category = object.find('name')
        bndbox = object.find('bndbox')  # 子节点下节点rank的值
        xmin = bndbox.find('xmin')  # type(xmin) = int
        xmax = bndbox.find('xmax')
        ymin = bndbox.find('ymin')
        ymax = bndbox.find('ymax')

        old_category, old_xmin, old_xmax, old_ymin, old_ymax = get_value(category, xmin, xmax, ymin, ymax)
        # ratio = calculate_ratio(width, height, old_xmin, old_xmax, old_ymin, old_ymax)             # 需要修改
        # if ratio<0.05:
        #     if old_category not in ['wfly', 'yculr', 'eggfly', 'healthy']:
        #         small+=1
        # if small > 3:
        #     SAVE=False
        if old_category in ["back", "healthy"]:    # remove instance class      # 需要修改
            parent = object.getparent()
            parent.remove(object)
        if category.text in ['spot', 'death', 'unknown']:
            print(old_category)
            category.text = 'physical_damage'

    if len(tree.findall('object')) == 0:
        SAVE=False

    if SAVE:
        tree.write(target_file, pretty_print=True, xml_declaration=False, encoding='utf-8')
    else:
        image_path = xml_file.replace('Annotations', 'JPEGImages')      # 需要修改
        image_path= image_path.replace('.xml', '.jpg')
        if os.path.exists(image_path):
            os.remove(image_path)


def run(xml_path=None, target=None):
    for roots, dirs, files in os.walk(xml_path):
        print(roots)
        target_dir = roots.replace('Annotations', target)
        if not os.path.exists(target_dir):              # 能够自动创建目标文件夹
            os.mkdir(target_dir)
        for file in files:
            if file.endswith('.xml'):
                file_path = os.path.join(roots, file)
                remove_instance(xml_file=file_path, target=target)

    print("Done!")


run(xml_path='/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/Annotations', target='NewAnnotations')      # 需要修改

