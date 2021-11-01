# Coding by SunWoo(tjsntjsn20@gmail.com)

import argparse

from utils.defaults import load_yaml, setup_configs
from utils.logger import build_logger
from data.transforms.build import build_transforms
from data.datasets.build import build_datasets
from data.loader.build import build_loader
from models.build import build_models
from engine.trainer import Trainer


def setting_args():
    parser = argparse.ArgumentParser(description='Training')
    parser.add_argument('--config_file', type=str, required=True, help='config file path for training based on yaml.')
    parser.add_argument('--gpu_id', type=int, default=0, help='a number of gpu')
    return parser.parse_args()

def train():
    # 0. setting configs
    args = setting_args()
    configs = load_yaml(args.config_file)
    configs = setup_configs(args, configs)

    # 1. setting logger
    logger = build_logger(configs)

    # 2. setting about data
    transforms = build_transforms(configs)
    datasets = build_datasets(configs)
    data_loader = build_loader(configs, datasets=datasets, transforms=transforms)

    # 3. setting models
    generator, discriminator = build_models(configs)

    # 4. setting trainer
    trainer = Trainer(configs, logger, data_loader, generator, discriminator)
    trainer.train()



if __name__ == '__main__':
    train()
