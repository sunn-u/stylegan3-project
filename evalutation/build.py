
from fvcore.common.registry import Registry

EVALUATION_REGISTRY = Registry("EVALUATION")
EVALUATION_REGISTRY.__doc__ = " Registry for Evaluation "

def build_evaluator(configs: dict):
    name = configs["EVALUATION"]["NAME"]
    evaluator = EVALUATION_REGISTRY.get(name)(configs)
    return evaluator
