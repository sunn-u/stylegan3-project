# Coding by SunWoo(tjsntjsn20@gmail.com)

from torch.utils.data import Dataset
from data.utils import load_image


class BasicLoader(Dataset):
    def __init__(self, datasets, image_type, transforms):
        self.datasets = datasets
        self.image_type = image_type
        self.transforms = transforms

    def __len__(self):
        return len(self.datasets)

    def __getitem__(self, idx):
        image_dir = self.datasets[idx]
        image = load_image(image_dir, self.image_type)
        if self.transforms is not None:
            image = self.transforms(image)
        return image
