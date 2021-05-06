from os import path
from threading import Thread

from utils import get_window_id, exec_shell_cmd
from frames2video import make_video

class WindowRecorder(Thread):

    def __init__(self, window_name, log_dir_path, log_name):
        super().__init__()
        self.term_flag = False
        self.window_id = get_window_id(window_name)
        self.log_dir_path = log_dir_path
        self.log_name = log_name
        print('Created recorder for window with name %s and id "%s"'
              % (window_name, self.window_id))
        print('Recorder log path: %s' % path.join(self.log_dir_path, self.log_name))
          
    def finish(self):
        self.term_flag = True
        
    def run(self):
        print('Recording started!')

        # Step 1: making screenshots
        frame_ind = 0
        while not self.term_flag:
            file_path = path.join(self.log_dir_path, self.log_name,
                                  f'frame_{frame_ind:04d}.png')
            print(file_path)
            exec_shell_cmd((f'import -window {self.window_id} {file_path}'))
            frame_ind += 1

        # Step 2: complile screenshots to the video
        make_video(
            frame_dir_path=path.join(self.log_dir_path, self.log_name),
            output_file_path=f'{path.join(self.log_dir_path, self.log_name)}.avi',
            fps=15,
        )
        
        print('Recording finished!')