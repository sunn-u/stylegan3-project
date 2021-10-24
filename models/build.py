
from fvcore.common.registry import Registry

GENERATOR_REGISTRY = Registry("GENERATOR")
GENERATOR_REGISTRY.__doc__ = " Registry for Generator"

DISCRIMINATOR_REGISTRY = Registry("DISCRIMINATOR")
DISCRIMINATOR_REGISTRY.__doc__ = " Registry for Discriminator"

def build_models(configs: dict):
    # build generator
    generator_name = configs["MODEL"]["GENERATOR"]["NAME"]
    generator = GENERATOR_REGISTRY.get(generator_name)(configs)
    generator = generator.to(configs["SOLVER"]["DEVICE"])

    # build discriminator
    discriminator_name = configs["MODEL"]["DISCRIMINATOR"]["NAME"]
    discriminator = DISCRIMINATOR_REGISTRY.get(discriminator_name)(configs)
    discriminator = discriminator.to(configs["SOLVER"]["DEVICE"])

    return generator, discriminator
