from os import path
import platform
from threading import Thread

from utils import get_window_id, exec_shell_cmd
import win32_utils
from frames2video import make_video

class WindowRecorder(Thread):

    # TODO: add ability to use only part (substring) of the target window name
    def __init__(self, window_name, log_dir_path, log_name):
        super().__init__()

        self.term_flag = False

        platform_name = platform.system()
        if platform_name == 'Windows':
            self.make_screenshot = lambda file_path: win32_utils.make_screenshot(window_name, file_path)
        elif platform_name == 'Linux':
            window_id = get_window_id(window_name)
            self.make_screenshot = lambda file_path: exec_shell_cmd(f'import -window {window_id} {file_path}')
        else:
            raise Exception('Not valid platform: %s' % platform_name)

        self.log_dir_path = log_dir_path
        self.log_name = log_name

        print('Created recorder for window with name %s' % window_name)
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
            self.make_screenshot(file_path)
            frame_ind += 1

        # Step 2: compile screenshots to the video
        print('Compiling video...')
        make_video(
            frame_dir_path=path.join(self.log_dir_path, self.log_name),
            output_file_path=f'{path.join(self.log_dir_path, self.log_name)}.avi',
            fps=15,
        )
        
        print('Recording finished!')