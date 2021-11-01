# Coding by SunWoo(tjsntjsn20@gmail.com)

import yaml
import torch

from data.types import Argparse


def load_yaml(config_path: str) -> yaml:
    with open(config_path, encoding='utf-8') as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)
    return configs

def setup_configs(args: Argparse, configs: dict) -> dict:
    configs["SOLVER"]["DEVICE"] = is_gpu(args)
    return configs

def is_gpu(args: Argparse):
    return torch.device(f'cuda:{args.gpu_id}' if torch.cuda.is_available() else 'cpu')
