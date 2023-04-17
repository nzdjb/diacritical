from unidecode import unidecode
from pywikibot import Site, Page
from typing import Set


class Search:
    _namespaces = [0]

    def __init__(self, site: Site = None):
        if not site:
            site = Site("en", "wikipedia")
        self._site = site

    def search(self, lookup_pattern: str) -> Set[Page]:
        lookup_pattern = unidecode(lookup_pattern).lower()
        result = self._site.search(
            lookup_pattern, namespaces=self._namespaces, content=True
        )
        return set(result)
