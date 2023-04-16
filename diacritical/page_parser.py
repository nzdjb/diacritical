from diacritical.config_parser import Config
from pywikibot import Page
from re import findall, sub, IGNORECASE
from unidecode import unidecode


class PageParser:
    def __init__(self, config: Config, page: Page) -> None:
        self.config = config
        self.page = page

    def candidate(self) -> bool:
        if self._page_ignored():
            return False
        content = self.page.get()
        for pattern in self.config.ignored_patterns:
            content = sub(pattern, "", content, flags=IGNORECASE)
        groups = findall(unidecode(self.config.name), content, flags=IGNORECASE)
        return len(groups) > 0

    def _page_ignored(self) -> bool:
        return str(self.page.title()) in self.config.ignored_pages
