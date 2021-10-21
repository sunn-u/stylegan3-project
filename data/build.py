
from fvcore.common.registry import Registry

DATA_LOADER_REGISTRY = Registry("DATA_LOADER")
DATA_LOADER_REGISTRY.__doc__ = " Registry for Data-Loader "

def build_loader(configs: dict):
    name = configs["DATA"]["NAME"]
    loader = DATA_LOADER_REGISTRY.get(name)(configs)
    return loader
