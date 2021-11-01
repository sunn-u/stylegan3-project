# Coding by SunWoo(tjsntjsn20@gmail.com)

'''
    Basic frame for Generator.
'''

import torch.nn as nn

from models.build import GENERATOR_REGISTRY
from models.generator.mapping_network import MappingNetwork
from models.generator.synthesis_network import SynthesisNetwork


@GENERATOR_REGISTRY.register()
class BasicGenerator(nn.Module):
    def __init__(self, configs):
        self.mapping_network = MappingNetwork(configs)
        self.synthesis_network = SynthesisNetwork(configs)

    def forward(self, x):
        x = self.mapping_network(x)
        x = self.synthesis_network(x)
        return x
