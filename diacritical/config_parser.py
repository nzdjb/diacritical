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
                self.config[key] = Config(key, value)
        return self

    def load_config_dir(self, path: str) -> Self:
        for config in os.listdir(path):
            self.load_config(os.path.join(path, config))
        return self


class Config:
    def __init__(self, name: str, params: dict | None = None):
        self.name = name
        params = params or {}
        self.skip = params.get("skip", False)
        self.ignored_pages = params.get("ignored_pages", [])
        self.ignored_patterns = params.get("ignored_patterns", [])

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Config):
            return all(
                [
                    __value is not None,
                    type(self) == type(__value),
                    self.name == __value.name,
                    self.skip == __value.skip,
                    self.ignored_pages == __value.ignored_pages,
                    self.ignored_patterns == __value.ignored_patterns,
                ]
            )
        return NotImplemented
