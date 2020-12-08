_base_ = '../faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

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

# TODO: Update model url after bumping to V2.0
load_from = 'https://s3.ap-northeast-2.amazonaws.com/open-mmlab/mmdetection/models/faster_rcnn_r50_fpn_1x_20181010-3d1b3351.pth'  # noqa
