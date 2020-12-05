# gtuav


**Report**: We have released our technical report @ [link](https://deadlink.com).

## Introduction

Automatic understanding of visual data collected from overhead platforms such as Drones or general UAVs have been increasingly prevalent to a wide range of applications, including government agencies, agricultural services, aerial photography, surveillance systems & more. Computer vision has been attracting increasing amounts of attention in this space due to factors in computation and data availability. Notable contributions in this space developed benchmarks and challenges such as Caltech [[1]()], KITTI [[2]()], ImageNet [[3]()], and MS COCO [[4]()] for object detection. 

In conjunction with ECCV & ICCV participants, the VisDrone team has constructed experimental dataset of images use for tracks for (1) image object detection, (2) video object detection, (3) single object tracking, and (4) multi-object tracking.

This repository contains instructions on building and redeploying our modeling efforts.

![demo image](resources/demo.jpg)

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

#### Demo

## Results

### Faster R-CNN

| Model  |    Backbone     |  Style  | Lr schd | Mem (GB) | Inf time (fps) | box AP | Config | Download |
| :----: | :-------------: | :-----: | :-----: | :------: | :------------: | :----: | :------: | :--------: |
| Faster-RCNN | S-50-FPN   | pytorch	|   1x	  |   4.8  |   -	          | 42.0 |[config](link) | [model](link) &#124; [log](link) |
| Faster-RCNN | S-101-FPN  | pytorch	|   1x	  |   7.1  |   -	          | 44.5 |[config](link) | [model](link) &#124; [log](link) |
| Center NET  | S-50-FPN   | pytorch	|   1x	  |   4.8  |   -	          | 42.0 |[config](link) | [model](link) &#124; [log](link) |
| Fast RCNN   | S-50-FPN   | pytorch	|   1x	  |   7.1  |   -	          | 44.5 |[config](link) | [model](link) &#124; [log](link) |
| Fast RCNN   | S-50-FPN   | pytorch	|   1x	  |   4.8  |   -	          | 42.0 |[config](link) | [model](link) &#124; [log](link) |
| Fast RCNN   | S-50-FPN   | pytorch	|   1x	  |   7.1  |   -	          | 44.5 |[config](link) | [model](link) &#124; [log](link) |

### Training Speed

The training speed is measure with s/iter. The lower, the better.

| Type         | mmdetection |
|--------------|-------------|
| Faster R-CNN |  0.216      |
| Mask R-CNN   |  0.265      |
| Retinanet    |  0.205      |

### Training memory

| Type         | mmdetection |
|--------------|-------------|
| Faster R-CNN | 3.8         |
| Mask R-CNN   | 3.9         |
| Retinanet    | 3.4         |


## License

This project is released under the [Apache 2.0 license](LICENSE).

## Changelog

v1.0.0 was released on December 5th, 2020.

## Citation

You can use the following to cite this work.

```
@article{mmdetection,
  title   = {{View from Above}: Assessing SOTA Techniques to Detect/Classify Objects in Real-Time Drone Feeds},
  author  = {Jayson Francis, Ryan Anderson, Mario Wijaya, Jing-Jing Li},
  journal= {arXiv preprint arXiv:XXXX},
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