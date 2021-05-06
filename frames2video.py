from os import path, listdir

import cv2

# run params
frame_dir_path = 'visual_logs/test/'
output_file_path = 'visual_logs/test.avi'
fps = 10

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

