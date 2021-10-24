
from data.loader.build import DATA_LOADER_REGISTRY
from data.utils import load_image


@DATA_LOADER_REGISTRY.register()
class FFHQ:
    def __init__(self, image_type, datasets, transforms):
        self.image_type = image_type
        self.datasets = datasets
        self.transforms = transforms

    def __len__(self):
        return len(self.datasets)

    def __getitem__(self, idx):
        image_dir = self.datasets[idx]
        image = load_image(image_dir, self.image_type)
        if self.transforms is not None:
            image = self.transforms(image)
        return image
