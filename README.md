# Open-world plant disease detection

* This code is an implementation of our manuscript: A New Deep Learning-based Dynamic Paradigm Towards Open-World Plant Disease Detection

* The manuscript is currently under peer review. We submitted it to Frontiers in Plant Science.
* Authors: Jiuqing Dong, Alvaro Fuentes, Sook Yoon*, Hyongsuk Kim*, Yongchae Jeong, Dong Sun Park



### Installation
* You can install the environment following this https://github.com/JosephKJ/OWOD
  
* Set up environment

    conda create -n OWPDD python=3.7

    conda activate OWPDD

    conda install pytorch==1.10.0 torchvision==0.11.0 torchaudio==0.10.0 cudatoolkit=11.3 -c pytorch -c conda-forge

* install dependecies

    pip install -r requirement.txt

* install mmdet (will take a while to process)

    unzip detectron2.zip

    python -m pip install -e ./

### Pre-trained model
* You can use our pre-trained model on [google drive](https://drive.google.com/drive/folders/1ru5TrhXtRzFcAgo9E2FSx8rRDTyxE5HZ?usp=sharing) to implement Well-trained UA-RPN in our work.
* If you use the Object365 model, please cite our paper. Other pre-trained models are from Detectron2.

### Note 
* We use Object365 pre-trained model to evaluate the OWOD task on the COCO dataset. We provide a part of the result at [COCO_RESULT.xlsx](https://github.com/JiuqingDong/OWPDD/blob/main/COCO.xlsx)
### train and test

* Kindly check run.sh file for a task workflow.

#### We will optimize our code and complete this documentation after our manuscript is accepted.


## How to use this code for a customer dataset?

Operational steps for the teacher-student learning paradigm:
step 0: Create your dataset, suffix of the annotation file should be '.xml'.
        If you don/t know how to transfer the Json to XML, please refer this: https://github.com/bot66/coco2voc
        
step 1: Put the customer dataset into ./datasets, the structure should be like this:

-..

-datasets

  -VOC2007
  
    -JPEGImages
    
      -000001.jpg *
    
    -Annotations
    
      -000001.xml *
    
    -ImageSets
    
      -Main
      
        -t1_train.txt ('.txt' file save the filename without suffix， eg. '000001')
        
        -t2_train.txt
        
        -t2_ft.txt
        
        ...
        
        -all_task_val.txt
        
        -all_task_test.txt
    
step 2: Change the config file, such as NUM_CLASSES, OWOD.CUR_INTRODUCED_CLS, PREV_INTRODUCED_CLS, and so on. You also can define your own dataset name. Note that the name matching at './detectron2/data/datasets/builtin.py'

step 3: Change the category names at './detectron2/data/datasets/pascal_voc.py'

step 4: Train the model. Kindly check run.sh file for a task workflow, and then run it. For example: 
- sh run.sh




