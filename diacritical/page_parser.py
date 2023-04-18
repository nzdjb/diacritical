from diacritical.config_parser import Config
from pywikibot import Page
from re import findall, sub, IGNORECASE
from unidecode import unidecode


class PageParser:
    def __init__(self, config: Config, page: Page) -> None:
        self.config = config
        self.page = page

    def candidate(self) -> bool:
        normal_name = unidecode(self.config.name)
        if self._page_ignored():
            return False
        content = self.page.get()
        for pattern in self.config.ignored_patterns:
            content = sub(pattern, "", content, flags=IGNORECASE)
        excluded_templates = "|".join(
            [
                "Proper name",
                "Not a typo",
                "Sic",
                "As written",
                "Typo",
                "Chem name",
                "Proper name",
            ]
        )
        content = sub(
            f"{{{{\s*(?:{excluded_templates})\s*\|{normal_name}}}}}",
            "",
            content,
            flags=IGNORECASE,
        )
        groups = findall(normal_name, content, flags=IGNORECASE)
        return len(groups) > 0

    def _page_ignored(self) -> bool:
        return str(self.page.title()) in self.config.ignored_pages
