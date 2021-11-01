# Coding by SunWoo(tjsntjsn20@gmail.com)

import torch.nn as nn

from models.build import DISCRIMINATOR_REGISTRY


@DISCRIMINATOR_REGISTRY.register()
class BasicDiscriminator(nn.Module):
    def __init__(self, configs):
        pass

    def forward(self, x):
        return x
