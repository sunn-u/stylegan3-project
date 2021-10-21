import torch
import torch.utils.data as data
from torch.utils.data.sampler import Sampler

from data.build import DATA_LOADER_REGISTRY

# todo : base 로더라서 baseloader 를 상속하는 다른 로더를 만든 후에 @DATA_LOADER ~ 옮기기
@DATA_LOADER_REGISTRY.register()
class BaseLoader(torch.utils.data.Dataset):
    def __init__(self, dataset):
        self.dataset = dataset

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        item = self.dataset[idx]
        return item
