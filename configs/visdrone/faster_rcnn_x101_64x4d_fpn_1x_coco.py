_base_ = '../faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
model = dict(
    pretrained='open-mmlab://resnext101_64x4d',
    backbone=dict(
        type='ResNeXt',
        depth=101,
        groups=64,
        base_width=4,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        style='pytorch'))

dataset_type = 'COCODataset'

classes = ('__background__', 'pedestrian', 'people', 'bicycle', 'car', 'van', 'truck', 'tricycle', 'awning-tricycle', 'bus', 'motor', 'others')

data = dict(
    train=dict(
        img_prefix='data/visdrone/train/',
        classes=classes,
        ann_file='data/visdrone/train/coco.json'),
    val=dict(
        img_prefix='data/visdrone/val/',
        classes=classes,
        ann_file='data/visdrone/val/coco.json'),
    test=dict(
        img_prefix='data/visdrone/test/',
        classes=classes,
        ann_file='data/visdrone/test/coco.json'))


