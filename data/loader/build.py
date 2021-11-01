# Coding by SunWoo(tjsntjsn20@gmail.com)

from fvcore.common.registry import Registry
from torch.utils.data import DataLoader

DATA_LOADER_REGISTRY = Registry("DATA_LOADER")
DATA_LOADER_REGISTRY.__doc__ = " Registry for Data-Loader "

def build_loader(configs: dict, **kwargs):
    name = configs["DATA"]["NAME"]
    image_type = configs["DATA"]["DATASET"]["TYPE"]
    data_sets = DATA_LOADER_REGISTRY.get(name)(image_type, **kwargs)
    loader = DataLoader(
        data_sets,
        batch_size=configs["SOLVER"]["BATCH_SIZE"],
        num_workers=configs["DATA"]["LOADER"]["NUM_WORKERS"],
        shuffle=configs["DATA"]["LOADER"]["SHUFFLE"]
    )
    return loader
