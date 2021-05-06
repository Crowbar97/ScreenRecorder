from record_frame import record_frame
from utils import get_window_geometry, get_window_id, window_is_open, bring2front


# for launching window recording
def record_window(window_name, fps, output_file_path, manual_geometry=None):
    # Step 1: getting geometry of the target window
    if manual_geometry is None:
        print('Detecting geometry...')
        window_id, left, top, width, height = get_window_geometry(window_name)
    else:
        print('Using manual geometry...')
        left, top, width, height = manual_geometry
        window_id = get_window_id(window_name)

    # Step 2: creating condition callback function
    # that checks whether target window is still open
    condition_callback = lambda: window_is_open(window_id)

    # Step 3: creating action callback function
    # that will bring target window to the front
    # each time we need to make screenshot
    # action_callback = lambda: bring2front(window_id)
    # or just bringing it once
    bring2front(window_id)

    # Step 4: running window recording
    record_frame(
        left, top, width, height,
        fps, output_file_path,
        condition_callback,
        # action_callback
    )


# usage example
if __name__ == '__main__':
    record_window(
        window_name='Home',
        fps=1,
        output_file_path='video_recordings/window_record.avi'
    )