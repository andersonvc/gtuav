_base_ = [
    '/home/jj/Documents/mmdetection/configs/_base_/models/retinanet_r50_fpn.py',
    '/home/jj/Documents/mmdetection/configs/_base_/default_runtime.py'
]
cudnn_benchmark = True
norm_cfg = dict(type='BN', requires_grad=True)
model = dict(
    pretrained='torchvision://resnet50',
    backbone=dict(
        type='ResNet',
        depth=50,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=norm_cfg,
        norm_eval=False,
        style='pytorch'),
    neck=dict(
        relu_before_extra_convs=True,
        no_norm_on_lateral=True,
        norm_cfg=norm_cfg),
    bbox_head=dict(type='RetinaSepBNHead', num_ins=5, norm_cfg=norm_cfg))
# training and testing settings
train_cfg = dict(assigner=dict(neg_iou_thr=0.5))
# dataset settings
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        type='Resize',
        img_scale=(640, 640),
        ratio_range=(0.8, 1.2),
        keep_ratio=True),
    dict(type='RandomCrop', crop_size=(640, 640)),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size=(640, 640)),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(640, 640),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=64),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
dataset_type = 'CocoDataset'
data_root = '../data/visdrone/'
data = dict(
    samples_per_gpu=8,
    workers_per_gpu=4,
    train=dict(
    	type=dataset_type,
    	ann_file=data_root + 'VisDrone2019-DET-train/coco.json',
        img_prefix=data_root + 'VisDrone2019-DET-train/images/',
        pipeline=train_pipeline),
    val=dict(
    	type=dataset_type,
    	ann_file=data_root + 'VisDrone2019-DET-val/coco.json',
        img_prefix=data_root + 'VisDrone2019-DET-val/images/',
    	pipeline=test_pipeline),
    test=dict(
    	type=dataset_type,
    	ann_file=data_root + 'VisDrone2019-DET-test-dev/coco.json',
        img_prefix=data_root + 'VisDrone2019-DET-test-dev/images/',
        pipeline=test_pipeline))
# optimizer
optimizer = dict(
    type='SGD',
    lr=0.08,
    momentum=0.9,
    weight_decay=0.0001,
    paramwise_cfg=dict(norm_decay_mult=0, bypass_duplicate=True))
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=1000,
    warmup_ratio=0.1,
    step=[30, 40])
# runtime settings
total_epochs = 20
