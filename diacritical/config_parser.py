from tomllib import load
import os


class ConfigParser:
    def __init__(self):
        self.config = {}

    def load_config(self, path):
        with open(path, "rb") as f:
            toml = load(f)
            for key, value in toml.items():
                self.config[key] = value
        return self

    def load_config_dir(self, path):
        for config in os.listdir(path):
            self.load_config(os.path.join(path, config))
        return self
