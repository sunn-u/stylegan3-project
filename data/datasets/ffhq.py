# Coding by SunWoo(tjsntjsn20@gmail.com)

'''
    Getting Data-set from FFHQ datasets.
'''

from data.datasets.build import DATASETS_REGISTRY
from data.utils import get_all_items


@DATASETS_REGISTRY.register()
def FFHQ(configs: dict):
    data_dir = configs["DATA"]["DATASET"]["ROOT_DIR"]
    img_extension = configs["DATA"]["DATASET"]["IMG_EXT"]
    data_file_list = get_all_items(data_dir, img_extension)
    return data_file_list
