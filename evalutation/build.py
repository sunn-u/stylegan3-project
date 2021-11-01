# Coding by SunWoo(tjsntjsn20@gmail.com)

from fvcore.common.registry import Registry

EVALUATION_REGISTRY = Registry("EVALUATION")
EVALUATION_REGISTRY.__doc__ = " Registry for Evaluation "

def build_evaluator(configs: dict):
    name = configs["EVALUATION"]["NAME"]
    evaluator = EVALUATION_REGISTRY.get(name)(configs)
    return evaluator



'''
            :param gt_images: batch, channel, height, width 형태의 tensor
            :param gt_masks:
            :param pred_masks:
        :return:
        '''