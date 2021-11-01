# Coding by SunWoo(tjsntjsn20@gmail.com)

from fvcore.common.registry import Registry

DATASETS_REGISTRY = Registry("DATASETS")
DATASETS_REGISTRY.__doc__ = " Registry for Datasets "

def build_datasets(configs: dict):
    name = configs["DATA"]["NAME"]
    loader = DATASETS_REGISTRY.get(name)(configs)
    return loader
