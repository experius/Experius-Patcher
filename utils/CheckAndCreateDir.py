import os


def check_and_create_dir(base_dir: str, dir_path: str):
    current_dir = base_dir
    dirs = dir_path.split('/')
    for dir_to_check in dirs:
        current_dir += '/' + dir_to_check
        if not os.path.exists(current_dir):
            os.makedirs(current_dir)
