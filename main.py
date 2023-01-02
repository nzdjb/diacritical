from pywikibot import Site
from re import findall, sub, IGNORECASE
from tomllib import load
from os import listdir, path

configs = {}
config_path = "config"
for config_name in listdir(config_path):
    with open(path.join(config_path, config_name), "rb") as f:
        toml = load(f)
        for name, config in toml.items():
            configs[name] = config

site = Site("en", "wikipedia")
for name, config in configs.items():
    if config.get("skip", False):
        continue
    print(f"{name}:")
    i = 0
    results = site.search(config["lookup_pattern"], namespaces=[0], content=True)
    for result in results:
        if str(result.title()) in config.get("ignored_pages", []):
            continue
        content = result.get()
        for pattern in config.get("ignored_patterns", []):
            content = sub(pattern, "", content, flags=IGNORECASE)
        groups = findall(
            ".{0,20}" + config["lookup_pattern"] + ".{0,20}", content, flags=IGNORECASE
        )
        if len(groups) > 0:
            i = i + 1
            print(f"{result.title()}: {result.full_url()}")
            if config.get("print_groups", False):
                print(groups)
    print(f"{i} articles with potential misspellings found.")
