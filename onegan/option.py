import argparse

import yaml
from easydict import EasyDict


class Parser():

    def __init__(self, description, config=None):
        self.config_file = config
        self.parser = argparse.ArgumentParser(description=description)
        self._add_default_option()

    def parse(self):
        base_cfg = self._load_option_config(self.config_file)
        cfg = vars(self.parser.parse_args())
        base_cfg.update({k: v for k, v in cfg.items() if v})
        return EasyDict(**base_cfg)

    def add_argument(self, *args, **kwargs):
        self.parser.add_argument(*args, **kwargs)

    def _add_default_option(self):
        trainer_option(self.parser)

    def _load_option_config(self, path):
        if not path:
            return {}
        with open(path) as f:
            return yaml.load(f)


def trainer_option(parser):
    parser.add_argument('--epoch', type=int)
    parser.add_argument('--batch_size', type=int)
    parser.add_argument('--lr', type=float)
    parser.add_argument('--worker', type=int)