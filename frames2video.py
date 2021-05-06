from os import path, listdir
import argparse

import cv2

def parse_args():
    parser = argparse.ArgumentParser("./train.py")
    parser.add_argument(
        '--frame_dir_path', '-i',
        type=str,
        required=True,
        help='Path to directory with frames need to compile for video',
    )
    parser.add_argument(
        '--output_file_path', '-o',
        type=str,
        required=True,
        help='Path to output video file',
    )
    parser.add_argument(
        '--fps',
        type=int,
        required=False,
        default=15,
        help='Output video FPS',
    )
    return parser.parse_args()


def make_video(frame_dir_path, output_file_path, fps):
    file_names = sorted(listdir(frame_dir_path))

    writer = cv2.VideoWriter(
        filename=output_file_path,
        fourcc=cv2.VideoWriter_fourcc(*'XVID'),
        fps=fps,
        frameSize=cv2.imread(path.join(frame_dir_path, file_names[0])).shape[:2]
    )

    for file_name in file_names:
        frame = cv2.imread(path.join(frame_dir_path, file_name), cv2.IMREAD_COLOR)
        writer.write(frame)

    writer.release()


if __name__ == '__main__':
    args = parse_args()
    make_video(args.frame_dir_path, args.output_file_path, args.fps)
