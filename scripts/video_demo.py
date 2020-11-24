import os
import os.path as osp
import shutil
from argparse import ArgumentParser

import mmcv
from tqdm import tqdm

from mmdet.apis import init_detector, inference_detector


def check_path_exist(path):
    if not osp.isdir(path):
        os.mkdir(path)


def main():
    parser = ArgumentParser()
    parser.add_argument('--video', help='video file')
    parser.add_argument('--config', help='Config file')
    parser.add_argument('--checkpoint', help='Checkpoint file')
    parser.add_argument(
        '--device', default='cuda:0', help='Device used for inference')
    parser.add_argument(
        '--score-thr', type=float, default=0.3, help='bbox score threshold')
    parser.add_argument(
        '--theme', type=str, default='white', help='themes to show detect results')
    args = parser.parse_args()

    # build the model from a config file and a checkpoint file
    model = init_detector(args.config, args.checkpoint, device=args.device)

    # test a video and show the results
    video = mmcv.VideoReader(args.video)
    result_root = "./results"
    check_path_exist(result_root)
    frame_dir = osp.join(result_root, 'frame')
    check_path_exist(frame_dir)
    frame_id = 0
    interal = len(video) // 13
    key_frame_path = "./key_frame"
    check_path_exist(key_frame_path)
    key_frame_dir = osp.join(key_frame_path, args.video.split('/')[-1].split('.')[0])
    check_path_exist(key_frame_dir)
    for frame in tqdm(video, ncols=64):
        result = inference_detector(model, frame)
        model.show_result(frame, result, score_thr=args.score_thr, out_file=osp.join(frame_dir, '{:06d}.jpg'.format(frame_id)))
        if (frame_id + 1) % interal == 0:
            shutil.copyfile(src=osp.join(frame_dir, '{:06d}.jpg'.format(frame_id)),
                            dst=osp.join(key_frame_dir, '{:06d}.jpg'.format(frame_id)))
        frame_id += 1
    output_video_path = osp.join(result_root, args.video.split('/')[-1])
    mmcv.frames2video(frame_dir, output_video_path, fourcc='mp4v', filename_tmpl='{:06d}.jpg')
    shutil.rmtree(frame_dir)


if __name__ == '__main__':
    main()
