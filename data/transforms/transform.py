# Coding by SunWoo(tjsntjsn20@gmail.com)

'''
    Functions of Data-Transforms.
'''


import torchvision.transforms.functional as F
from torchvision.transforms.functional import _interpolation_modes_from_int


class Crop:
    def __init__(self, size: int):
        self.size = size

    def __call__(self, image):
        return F.center_crop(image, self.size)

class Resize:
    def __init__(self, size: int, mode: int):
        self.size = size
        self.mode = _interpolation_modes_from_int(mode)

    def __call__(self, image):
        return F.reisze(image, (self.size, self.size), self.mode)

class ToTensor:
    def __call__(self, image):
        return F.to_tensor(image)
