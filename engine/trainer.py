# Coding by SunWoo(tjsntjsn20@gmail.com)

class Trainer:
    def __init__(self, configs, logger, data_loader, generator, discriminator):
        self.configs = configs
        self.logger = logger
        self.data_loader = data_loader
        self.generator = generator
        self.discriminator = discriminator

        self.init_for_generator(configs)
        self.init_for_discriminator(configs)

    def init_for_generator(self, configs):
        pass
        # self.generator_criterion
        # self.generator_optimizer

    def init_for_discriminator(self, configs):
        pass
        # self.discriminator_criterion
        # self.discriminator_optimizer

    def train(self):
        pass
