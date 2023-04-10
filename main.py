from re import findall, sub, IGNORECASE
from unidecode import unidecode
from diacritical.config_parser import ConfigParser
from diacritical.search import Search

config_path = "config"
configs = ConfigParser().load_config_dir(config_path).config

# TODO: Improve CLI.
# TODO: Improve output.

site = Search()
for name, config in configs.items():
    if config.skip:
        continue
    print(f"{name}:")
    i = 0
    results = site.search(name)
    for result in results:  # TODO: Multithread, create processing class.
        if str(result.title()) in config.ignored_pages:
            continue
        content = result.get()
        for pattern in config.ignored_patterns:
            content = sub(pattern, "", content, flags=IGNORECASE)
        groups = findall(
            ".{0,20}" + unidecode(name) + ".{0,20}", content, flags=IGNORECASE
        )
        if len(groups) > 0:
            i = i + 1
            print(f"{result.title()}: {result.full_url()}")
    print(f"{i} articles with potential misspellings found.")
