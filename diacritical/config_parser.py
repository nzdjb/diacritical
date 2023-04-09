from tomllib import load
from typing import Self
import os


class ConfigParser:
    def __init__(self):
        self.config = {}

    def load_config(self, path: str) -> Self:
        with open(path, "rb") as f:
            toml = load(f)
            for key, value in toml.items():
                self.config[key] = value
        return self

    def load_config_dir(self, path: str) -> Self:
        for config in os.listdir(path):
            self.load_config(os.path.join(path, config))
        return self
