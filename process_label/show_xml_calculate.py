
import xml.etree.ElementTree as ET
import cv2
import os
from tqdm import tqdm

xml_path = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/Annotations'     # 你的xml文件路径
# img_path = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/JPEGImages'         # 图像路径
img_path = "/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/Inference"
img_xml  = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/showxml/'       # 显示标注框保存该文件的路径
# all_class = {'blossom_end_rot', 'graymold', 'powdery_mildew', 'spider_mite', 'spotting_disease', 'healthy', 'background'}
all_class = {"physical_damage": 0, "canker": 1, "plague": 2, "wilt": 3, "yculr": 4, "miner": 5, "lmold": 6, "tocv": 7, "stress": 8, "powder": 9,
            "gmold": 10, "wfly": 11, "eggfly": 12, "old": 13, "magdef": 14, "blossom_end_rot": 15, "graymold": 16, "powdery_mildew":17, "spider_mite":18, "spotting_disease":19}
all_instance = []

rename = {
    "magdef": "magnesium deficiency", "gmold":"gray_mold", "lmold":"leaf mold", "yculr": "yellow leaf curl virus", "physical_damage":"physical damage",

     "canker": "canker", "plague": "plague", "miner": "leaf miner", "wfly": "white fly", "eggfly": "white fly egg",

    "wilt": "wilt", "tocv": "chlorosis virus", "stress": "stress", "powder": "powdery_mildew", "old" :"old leaf",

    "blossom_end_rot": "blossom end rot", "graymold":  "gray mold", "powdery_mildew":"powdery mildew", "spider_mite": "spider mite", "spotting_disease":"spotting disease",
}

for name in tqdm(os.listdir(xml_path)):
    image_name = os.path.join(img_path, name.split('.')[0] + '.jpg')
    if os.path.exists(image_name):
        # 打开xml文档
        tree = ET.parse(os.path.join(xml_path,name))
        img = cv2.imread(image_name)
        box_thickness = int((img.shape[0] + img.shape[1])/1000) + 1  # 标注框的一个参数。本人图像大小不一致，在不同大小的图像上展示不同粗细的bbox
        text_thickness = box_thickness
        text_size = float(text_thickness/2)   # 显示标注类别的参数。字体大小。这些不是重点。不想要可以删掉。
        font = cv2.FONT_HERSHEY_SIMPLEX
        # 得到文档元素对象
        root = tree.getroot()
        allObjects = root.findall('object')
        if len(allObjects) == 0:
            print("1 :", name)
            _image_name = str(image_name)
            _xml_name = _image_name.replace('.jpg', '.xml')
            _xml_name = _xml_name.replace('train', 'train_xml')
            if os.path.exists(_image_name):
                # os.remove(_image_name)
                print(_image_name)
            else:
                print("=========", _image_name)
            if os.path.exists(_xml_name):
                #os.remove(_xml_name)
                print(_xml_name)

            else:
                print("=========", _xml_name)
            continue
        for i in range(len(allObjects)):    # 遍历xml标签，画框并显示类别。
            object = allObjects[i]
            objectName = object.find('name').text

            all_instance.append(objectName)
            xmin = int(object.find('bndbox').find('xmin').text)
            ymin = int(object.find('bndbox').find('ymin').text)
            xmax = int(object.find('bndbox').find('xmax').text)
            ymax = int(object.find('bndbox').find('ymax').text)
            objectName_replace = rename[objectName]
            cv2.putText(img, objectName_replace, (xmin, ymax), font, text_size, (0,0,0), text_thickness)
            cv2.rectangle(img,(xmin, ymin),(xmax, ymax),[255,255,255],box_thickness)
            if len(allObjects) == 0:
                print("error")

        name = name.replace('xml', 'jpg')
        img_save_path = os.path.join(img_xml, name)
        cv2.imwrite(img_save_path, img)

for key in all_class:
    print(key, all_instance.count(key))

'''
import os
import xml.etree.ElementTree as ET

def count_instances(voc_dir, class_order):
    class_counts = {}
    # 初始化类别计数为0
    for class_name in class_order:
        class_counts[class_name] = 0

    # 遍历VOC数据集中的每个XML文件
    for root, dirs, files in os.walk(voc_dir):
        for file in files:
            print(root, file)
            if file.endswith('.xml'):
                xml_file = os.path.join(root, file)
                # 解析XML文件
                tree = ET.parse(xml_file)
                roots = tree.getroot()

                # 查找所有的"object"元素
                objects = roots.findall('object')
                for obj in objects:
                    # 查找"name"元素并统计每个类别的实例数
                    name = obj.find('name')
                    class_name = name.text
                    if class_name in class_order:
                        class_counts[class_name] += 1

    return class_counts

# 调用函数统计实例数量
voc_dir = '/Users/jiuqingdong/Documents/Pycharm_Project_Code/OWOD-Plant/datasets/VOC2007/Annotations'
class_order = ["magdef", "gmold", "lmold", "yculr", "physical_damage",
                    "canker", "plague", "miner", "wfly", "eggfly",
                    "wilt", "tocv", "stress", "powder", "old",
               "blossom_end_rot", "graymold", "powdery_mildew", "spider_mite", "spotting_disease",
               ]
instance_counts = count_instances(voc_dir, class_order)

# 打印每个类别的实例数量
for class_name, count in instance_counts.items():
    print(f'{class_name}: {count} instances')

'''