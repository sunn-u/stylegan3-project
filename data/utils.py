# Coding by SunWoo(tjsntjsn20@gmail.com)

import os
import glob
from PIL import Image

from data.types import PIL


def get_all_items(directory: str, img_ext: list):
    file_list = []
    for ext in img_ext:
        file_list += glob.glob(f'{directory}/**/*.{ext}', recursive=True)
    return file_list

def load_image(directory: str, type: str) -> PIL:
    image = Image.open(directory)
    if type == 'RGB':
        return image.convert('RGB')
    if type == 'GRAY':
        return image.convert('L')
