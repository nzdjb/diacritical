from diacritical.config_parser import ConfigParser
from diacritical.search import Search
from diacritical.page_parser import PageParser

config_path = "config"
configs = ConfigParser().load_config_dir(config_path).config

# TODO: Improve CLI.
# TODO: Improve output.

site = Search()
for config in configs.values():
    if config.skip:
        continue
    print(f"{config.name}:")
    i = 0
    results = site.search(config.name)
    for result in results:  # TODO: Multithread.
        parser = PageParser(config, result)
        if parser.candidate():
            i = i + 1
            print(f"{result.title()}: {result.full_url()}")
    print(f"{i} articles with potential misspellings found.")
