import os
import glob


def get_all_items(directory: str):
    file_list = []
    IMG_EXT = ['**/*.jpg', '**/*.png']
    for ext in IMG_EXT:
        file_list += glob.glob(f'{directory}/{ext}', recursive=True)

    return file_list
