# Georgia Tech UAV

| [Deep Learning Fall 2020 at Georgia Tech (Prof. Zsolt Kira)](https://github.com/pytorch/workshops/tree/master/CS7643)


**Report**: We have released our technical report [here](report/rgtax04882052020.pdf).

## Introduction

Automatic understanding of visual data collected from overhead platforms such as Drones or general UAVs have been increasingly prevalent to a wide range of applications, including government agencies, agricultural services, aerial photography, surveillance systems & more. Computer vision has been attracting increasing amounts of attention in this space due to factors in computation and data availability. Notable contributions in this space developed benchmarks and challenges such as Caltech [[1]()], KITTI [[2]()], ImageNet [[3]()], and MS COCO [[4]()] for object detection.

In conjunction with ECCV & ICCV participants, the VisDrone team has constructed experimental dataset of images use in challenges for (1) image object detection, (2) video object detection, (3) single object tracking, and (4) multi-object tracking.

This repository contains instructions on how to evaluate state-of-the-art modeling architectures with mmdetection framework and aerial imagery.

[![watch demo](https://img.youtube.com/vi/83NDDz0zbiY/hqdefault.jpg)](https://www.youtube.com/watch?v=83NDDz0zbiY)

## Dataset

The VisDrone dataset is colleted by the AISKYEYE team at the Lab of Machine Learning & Data Mining, Tianjin University, China. The benchmark dataset consists of 288 video clips formed by 261,908 frames and 10,209 images taken from 14 different cities in china. More information can be found http://aiskyeye.com/.

                                                            Number of images
    ---------------------------------------------------------------------------------------------------
      Dataset                            Training              Validation            Test-Challenge
    ---------------------------------------------------------------------------------------------------
      Object detection in images       6,471 images            548 images             1,580 images
    ---------------------------------------------------------------------------------------------------

In addition to the standard noramlized bbox annotations (i.e ``bbox_left/top/width/height``) visdrone also contains `truncation` and `occlusion` identifiers as described below.

        Name                                                  Description
    -------------------------------------------------------------------------------------------------------------------------------

    <object_category> The object category indicates the type of annotated object, (i.e., ignored regions(0), pedestrian(1), people(2), bicycle(3), car(4), van(5), truck(6), tricycle(7), awning-tricycle(8), bus(9), motor(10), others(11))

    <truncation> The score in the DETECTION result file should be set to the constant -1.
    The score in the GROUNDTRUTH file indicates the degree of object parts appears outside a frame
    (i.e., no truncation = 0 (truncation ratio 0%), and partial truncation = 1 (truncation ratio 1% ~ 50%)).

    <occlusion>	The score in the DETECTION file should be set to the constant -1. The score in the GROUNDTRUTH file indicates the fraction of objects being occluded (i.e., no occlusion = 0 (occlusion ratio 0%), partial occlusion = 1 (occlusion ratio 1% ~ 50%), and heavy occlusion = 2 (occlusion ratio 50% ~ 100%)).
   ------------------------------------------------------------------------------------------------------------------------------


## Installation

1. Create a virtualized environment.

```
conda create -n gtdl python=3.7 -y
conda activate gtdl
```

2. Install dependencies

```
conda install pytorch torchvision -c pytorch
```

3. Install mmcv and mmdetection frameworks.

```
pip install mmcv-full
```

```
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection

pip install -r requirements/build.txt
pip install -v -e .  # or "python setup.py develop"
```


## Getting Started

#### Training

Refer to `baseline` directory for our general pipeline.

```
python baseline/train_baseline
```

You can also leverage mmdetection cli

```
python mmdetection/tools/train.py <configfile.py>
```

#### Demo

To run inference on a video, you can use the following `video_demo.py` script as follows:

```
python scripts/video_demo.py --video <videofile.mp4> --config <configfile.py> --checkpoint <latest.pth>
```

#### Evaluation

To evaluate mAP and class performance:
```
python mmdetection/tools/test.py <configfile.py> <latest.pth> --eval bbox --options "classwise=True"
```

To evaluate model fps performance:
```
python mmdetection/tools/benchmark.py <configfile.py> <latest.pth>
```

To evaluate model floating point operations and number of parameters:
```
python mmdetection/tools/get_flops.py <configfile.py>
```

## Results

### GT UAV Model Zoo

| Model  |    Backbone     |  Style  | Lr schd | Mem (GB) | Inf time (fps) | box AP | Config | Download |
| :----: | :-------------: | :-----: | :-----: | :------: | :------------: | :----: | :------: | :--------: |
| Faster-RCNN (CE)   | S-50-FPN   | pytorch	|   1x	  |   4.8    |   23	          | 24.3 |[config](configs/visdrone/) | [model](link) &#124; [log](link) |
| Faster-RCNN (FOCAL)  | S-50-FPN   | pytorch	|   1x	  |   4.8  |   23	          | 22.5 |[config](configs/visdrone/faster_rcnn_r50_fpn_focal_l1loss_1x_coco.py) | [model](https://drive.google.com/drive/folders/1lmsgS1Z152tMRIHfEDG1cgkLxWKCa733?usp=sharing) &#124; [log](logs/faster_rcnn_r50_fpn_focal_l1loss_1x_coco/) |
| ~~Faster-RCNN~~   | ~~S-101-FPN~~  | ~~pytorch~~	|   ~~1x~~	  |   ~~8.1~~  |   ~~18~~	          | ~~17.9~~ |[config](configs/visdrone/faster_rcnn_x101_64x4d_fpn_1x_coco.py) | [model](link) &#124; [log](logs/faster_rcnn_x101_64x4d_fpn_1x_coco/) |
| Cascade RCNN  | S-50-FPN   | pytorch	|   1x	  |   4.8  |   13	          | 32.9 |[config](configs/visdrone/cascade_rcnn_r50_fpn_1x_coco.py) | [model](https://drive.google.com/open?id=1aacfxzj1FoRKBM8Fa-FFw4WCK64SfFp-) &#124; [log](logs/cascade_rcnn_r50_fpn_1x_coco/) |
| DetectoRS     | S-50-FPN   | pytorch	|   1x	  |   4.1  |   11	          | 20.6 |[config](link) | [model](https://drive.google.com/open?id=1pC2QvMw-S9fLFIhUMtb-TYwZXJL8q7_v) &#124; [log](logs/cascade_rcnn_detector/) |

### Training Speed

The training speed is measure with s/iter. The lower, the better.

| Type         | mmdetection |
|--------------|-------------|
| Faster R-CNN |  0.216      |
| Cascade R-CNN   |  0.198      |
| Retinanet    |  0.205      |


### Training memory

| Type         | mmdetection |
|--------------|-------------|
| Faster R-CNN | 3.8         |
| Cascade R-CNN   | 4.3         |
| Retinanet    | 3.4         |

## Extra: Generating stylized examples.

1) Download stylized images

Use kaggle to download painters-by-numbers dataset directly at https://www.kaggle.com/c/painter-by-numbers/data. or if you have `kaggle` api installed you can use:

`kaggle datasets download mfekadu/painters-train-part-1/2/3`

2) Download autoencoder networks and generate data.

```
git clone https://github.com/bethgelab/stylize-datasets
cd stylized-datasets
```

then run the following command to generate your augmented dataset.

```
 python3 stylize.py
      --content-dir '/home/username/stylize-datasets/images/'
      --style-dir '/home/username/stylize-datasets/train/'
      --num-styles 10
      --alpha 0.5
      --content_size 0
      --style_size 256
 ```

## License

This project is released under the [Apache 2.0 license](LICENSE).

## Changelog

v1.0.0 was released on December 5th, 2020.

## Citation

You can use the following to cite this work.

```
@article{gtuav,
  title   = {{View from Above}: Assessing SOTA Techniques to Detect/Classify Objects in Real-Time Drone Feeds},
  author  = {Jayson Francis, Ryan Anderson, Mario Wijaya, Jing-Jing Li},
  journal= {},
  year={2020}
}
```

## Contributing

This repository is currently maintained by the following:

Jayson Francis ([@jaysonfrancis](https://github.com/jaysonfrancis))

Ryan Anderson ([@ryananderson](https://github.com/))

Mario Wijaya ([@mariowijaya](https://github.com/))

Jing-Jing Li ([@jingjingli](https://github.com))

We appreciate all contributions. Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing guideline.
