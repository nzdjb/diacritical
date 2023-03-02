from unidecode import unidecode
from pywikibot import Site
from pywikibot.data.api import PageGenerator

class Search:
    _namespaces=[0]
    
    def __init__(self, site: Site=None):
        if not site:
            site = Site("en", "wikipedia")
        self._site = site

    def search(self, lookup_pattern: str) -> PageGenerator:
        lookup_pattern = unidecode(lookup_pattern).lower()
        return self._site.search(lookup_pattern, namespaces=self._namespaces, content=True)
