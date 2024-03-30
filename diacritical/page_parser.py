from diacritical.config_parser import Config
from pywikibot import Page
from re import findall, sub, IGNORECASE
from unidecode import unidecode


class PageParser:
    def __init__(self, config: Config, page: Page) -> None:
        self.config = config
        self.page = page
        self.normal_name = unidecode(self.config.name)

    def candidate(self) -> bool:
        if self._page_ignored():
            return False
        content = self.page.get()
        content = self._remove_ignored_patterns(content)
        content = self._remove_excluded_templates(content)
        content = self._remove_urls(content)
        groups = findall(self.normal_name, content, flags=IGNORECASE)
        return len(groups) > 0

    def _page_ignored(self) -> bool:
        return str(self.page.title()) in self.config.ignored_pages

    def _remove_excluded_templates(self, content) -> str:
        excluded_templates = "|".join(
            [
                "Proper name",
                "Not a typo",
                "Sic",
                "As written",
                "Typo",
                "Chem name",
            ]
        )
        content = sub(
            rf"{{{{\s*(?:{excluded_templates})\s*\|{self.normal_name}}}}}",
            "",
            content,
            flags=IGNORECASE,
        )
        return content

    def _remove_ignored_patterns(self, content) -> str:
        for pattern in self.config.ignored_patterns:
            content = sub(pattern, "", content, flags=IGNORECASE)
        return content

    def _remove_urls(self, content) -> str:
        content = sub(
            r"url\s*=\s*\S*\s*[}|]",
            "",
            content,
            flags=IGNORECASE,
        )
        return content
