# Coding by SunWoo(tjsntjsn20@gmail.com)

'''
    Codes for logger : build
'''


import os
import logging
from logging.handlers import TimedRotatingFileHandler

from data.types import Logging


def build_logger(configs: dict) -> Logging:
    logger = logging.getLogger(__name__)
    logger.setLevel(configs['SOLVER']['LOG']['LEVEL'])
    formatter = logging.Formatter(
        '[%(asctime)s] [%(filename)s > %(funcName)s > %(lineno)d] : %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    log_dir = os.path.join(configs['OUTPUT_DIR'], 'logs')
    os.makedirs(log_dir, exist_ok=True)

    SH = logging.StreamHandler()
    SH.setFormatter(formatter)
    logger.addHandler(SH)

    FH = TimedRotatingFileHandler(
        filename=os.path.join(log_dir, 'log.log'),
        when='midnight',
        encoding='utf-8'
    )
    FH.setFormatter(formatter)
    FH.suffix = '%Y%m%d'
    logger.addHandler(FH)

    return logger
