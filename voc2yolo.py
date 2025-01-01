# 我是土堆 - www.xiaotudui.com

"""
将 VOC 数据集格式 转换为 YOLO 格式
"""

import os
import xml.etree.ElementTree as ET
from glob import glob


def convert_voc_to_yolo(xml_file, class_names):
    """
    将单个VOC格式的XML文件转换为YOLO格式
    
    Args:
        xml_file: XML文件路径
        class_names: 类别名称列表
    
    Returns:
        转换后的YOLO格式标注列表
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # 获取图像尺寸
    size = root.find('size')
    img_width = float(size.find('width').text)
    img_height = float(size.find('height').text)

    yolo_annotations = []

    # 处理每个目标
    for obj in root.findall('object'):
        # 获取类别名称
        class_name = obj.find('name').text

        # 获取类别索引
        if class_name not in class_names:
            continue
        class_idx = class_names.index(class_name)

        # 获取边界框坐标
        bbox = obj.find('bndbox')
        xmin = float(bbox.find('xmin').text)
        ymin = float(bbox.find('ymin').text)
        xmax = float(bbox.find('xmax').text)
        ymax = float(bbox.find('ymax').text)

        # 转换为YOLO格式 (x_center, y_center, width, height)
        x_center = (xmin + xmax) / (2.0 * img_width)
        y_center = (ymin + ymax) / (2.0 * img_height)
        width = (xmax - xmin) / img_width
        height = (ymax - ymin) / img_height

        # 确保值在0-1范围内
        x_center = min(max(x_center, 0), 1)
        y_center = min(max(y_center, 0), 1)
        width = min(max(width, 0), 1)
        height = min(max(height, 0), 1)

        yolo_annotations.append(f"{class_idx} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

    return yolo_annotations


def convert_dataset(xml_dir, output_dir, class_names):
    """
    转换整个数据集
    
    Args:
        xml_dir: 包含XML文件的目录
        output_dir: YOLO格式标注文件的输出目录
        class_names: 类别名称列表
    """
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 获取所有XML文件
    xml_files = glob(os.path.join(xml_dir, "*.xml"))

    for xml_file in xml_files:
        # 转换标注
        print(f"开始处理 {xml_file}")
        yolo_annotations = convert_voc_to_yolo(xml_file, class_names)

        # 生成输出文件名
        base_name = os.path.splitext(os.path.basename(xml_file))[0]
        txt_file = os.path.join(output_dir, f"{base_name}.txt")

        # 保存YOLO格式的标注
        with open(txt_file, 'w') as f:
            f.write('\n'.join(yolo_annotations))


if __name__ == "__main__":
    # VOC2007 和 2012数据集的20个类别
    class_names = [
        'aeroplane', 'bicycle', 'bird', 'boat', 'bottle',
        'bus', 'car', 'cat', 'chair', 'cow',
        'diningtable', 'dog', 'horse', 'motorbike', 'person',
        'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor'
    ]
    # 设置输入输出目录
    xml_dir = r"D:\xiaotudui\Dataset\VOC-2007\VOCtrainval_06-Nov-2007\VOCdevkit\VOC2007\Annotations"  # VOC格式XML文件目录
    output_dir = r"D:\xiaotudui\Dataset\VOC-2007\VOCtrainval_06-Nov-2007\VOCdevkit\VOC2007\YOLO"  # YOLO格式标注输出目录

    # 执行转换
    convert_dataset(xml_dir, output_dir, class_names)
    print("转换完成！")
