import torch.utils.data as data
from torch.utils.data.sampler import Sampler


class _MapIterableDataset(data.IterableDataset):