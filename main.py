from diacritical.config_parser import ConfigParser
from diacritical.search import Search
from diacritical.page_parser import PageParser
from functools import reduce

def cli():
    config_path = "config"
    configs = ConfigParser().load_config_dir(config_path).config

    # TODO: Improve CLI.
    # TODO: Improve output.

    site = Search()
    for config in configs.values():
        if config.skip:
            continue
        print(f"{config.name}:")
        results = site.search(config.name)
        candidates = map(
            lambda result: PageParser(config, result).candidate() and result or False,
            results,
        )
        candidates = reduce(lambda acc, i: acc + (i and [i] or []), candidates, [])
        for c in candidates:
            print(f"{c.title()}: {c.full_url()}")
        print(f"{len(candidates)} articles with potential misspellings found.")

if __name__ == '__main__':
    cli()
