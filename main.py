from pywikibot import Site
from re import findall, sub, IGNORECASE
from tomllib import load
from os import listdir, path
from unidecode import unidecode
from diacritical.config import Config
from diacritical.search import Search

config_path = "config"
config = Config()
config.load_config_dir(config_path)
configs = config.config

site = Search()
for name, config in configs.items():
    if config.get("skip", False):
        continue
    print(f"{name}:")
    i = 0
    results = site.search(name)
    for result in results:
        if str(result.title()) in config.get("ignored_pages", []):
            continue
        content = result.get()
        for pattern in config.get("ignored_patterns", []):
            content = sub(pattern, "", content, flags=IGNORECASE)
        groups = findall(
            ".{0,20}" + unidecode(name) + ".{0,20}", content, flags=IGNORECASE
        )
        if len(groups) > 0:
            i = i + 1
            print(f"{result.title()}: {result.full_url()}")
            if config.get("print_groups", False):
                print(groups)
    print(f"{i} articles with potential misspellings found.")
