_base_ = '../cascade_rcnn/cascade_rcnn_r50_fpn_20e_coco.py'
model = dict(
    type='CascadeRCNN',
    pretrained=None, # 'open-mmlab://resnext101_64x4d',
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

# optimizer_config = dict(grad_clip=dict(max_norm=35, norm_type=2))

dataset_type = 'COCODataset'

classes = ('pedestrian','people','bicycle','car','van','truck','tricycle','awning-tricycle','bus','motor')

data = dict(
    train=dict(
        img_prefix='configs/visdrone/train/',
        classes=classes,
        ann_file='configs/visdrone/train/annotation_coco.json'),
    val=dict(
        img_prefix='configs/visdrone/val/',
        classes=classes,
        ann_file='configs/visdrone/val/annotation_coco.json'),
    test=dict(
        img_prefix='configs/visdrone/val/',
        classes=classes,
        ann_file='configs/visdrone/val/annotation_coco.json'))

# runtime
lr_config = dict(warmup_ratio=0.1, step=[65, 71])
total_epochs = 73
