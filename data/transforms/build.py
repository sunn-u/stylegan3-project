# Coding by SunWoo(tjsntjsn20@gmail.com)

'''
    Codes for building Transforms.
'''


from data.transforms.transform import Resize, Crop, ToTensor


class Compose:
    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, image):
        for t in self.transforms:
            image = t(image)
        return image

def build_transforms(configs: dict):
    return Compose([
        Resize(configs["TRANSFORMS"]["RESIZE"]["SIZE"], configs["TRANSFORMS"]["RESIZE"]["MODE"]),
        Crop(configs["CROP"]),
        ToTensor()
    ])
