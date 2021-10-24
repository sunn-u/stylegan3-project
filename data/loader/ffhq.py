
from data.loader.build import DATA_LOADER_REGISTRY
from data.loader.common import BasicLoader


@DATA_LOADER_REGISTRY.register()
class FFHQ(BasicLoader):
    def __init__(self, image_type, datasets, transforms):
        super().__init__(datasets=datasets, image_type=image_type, transforms=transforms)

    def __len__(self):
        super().__len__()

    def __getitem__(self, idx):
        super().__getitem__(idx=idx)
