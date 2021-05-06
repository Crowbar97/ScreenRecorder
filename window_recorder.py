from os import path
from threading import Thread

from utils import get_window_id, exec_shell_cmd

class WindowRecorder(Thread):

    def __init__(self, window_name, output_dir_path='visual_logs/test/'):
        super().__init__()
        self.term_flag = False
        self.window_id = get_window_id(window_name)
        self.output_dir_path = output_dir_path
        print('Created recorder for window with name %s and id "%s"'
              % (window_name, self.window_id))
        print('Recorder log path: %s' % output_dir_path)
          
    def finish(self):
        self.term_flag = True
        
    def run(self):
        print('Recording started!')
        frame_ind = 0
        while not self.term_flag:
            file_path = path.join(self.output_dir_path, f'frame_{frame_ind:04d}.png')
            print(file_path)
            exec_shell_cmd((f'import -window {self.window_id} {file_path}'))
            frame_ind += 1
        print('Recording finished!')