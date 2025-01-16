# VOC2YOLO
Convert VOC Dataset Format to YOLO Format - 将 VOC 数据集的格式转换为 YOLO 格式

1. 提供将 VOC 数据集格式转换到 YOLO 格式的 python 代码。
2. 提供将 VOC 数据集格式转换到 YOLO 格式的 跨平台图形化界面。

https://www.xiaotudui.com/docs/tutorials/object-detection/dataset/dataset-label-format

## Python 代码使用说明

1. 准备 VOC 数据集，或者是 VOC格式标注的自制数据集。
2. 修改 `voc2yolo.py` 中的两处文件夹地址 (`xml_dir` 和 `output_dir`) 
   1.  `xml_dir` ，指定 VOC 数据集的标注文件所在文件夹。
   2.  `output_dir` ，指定 转换为YOLO格式的标注文件所要存储的文件夹。
   ```python
   xml_dir = r"D:\xiaotudui\Dataset\VOC-2007\VOCtrainval_06-Nov-2007\VOCdevkit\VOC2007\Annotations"  # VOC格式XML文件目录
   output_dir = r"D:\xiaotudui\Dataset\VOC-2007\VOCtrainval_06-Nov-2007\VOCdevkit\VOC2007\YOLO"  # YOLO格式标注输出目录
   ```
   这个例子中，就是将 `D:\xiaotudui\Dataset\VOC-2007\VOCtrainval_06-Nov-2007\VOCdevkit\VOC2007\Annotations` 文件夹下的 VOC 格式标注文件 转换为 YOLO 格式标注文件，并存储到 `D:\xiaotudui\Dataset\VOC-2007\VOCtrainval_06-Nov-2007\VOCdevkit\VOC2007\YOLO` 文件夹下。

   ⚠️  **注意：将文件夹地址粘贴到`xml_dir`和`output_dir`的时候，确保只替换`r""`双引号的内容。不要删除r和双引号。只需要替换双引号中间的内容即可。**
3. 运行 voc2yolo.py ，等待运行完成。


## 跨平台图形化界面使用说明




