class _EmptyMapDataset(torch.utils.data.Dataset):
    """
    Map anything to emptiness.
    """

    def __init__(self, dataset):
        self.ds = dataset

    def __len__(self):
        return len(self.ds)

    def __getitem__(self, idx):
        _ = self.ds[idx]
        return [0]