from unittest import TestCase
from unittest.mock import Mock
from pywikibot import Site
from diacritical.search import Search


class TestSearch(TestCase):
    def test_construct_search(self):
        s = Search()
        self.assertEqual(s._site, Site("en", "wikipedia"))

    def test_construct_search_with_site(self):
        m = Mock()
        s = Search(m)
        self.assertEqual(s._site, m)

    def test_search(self):
        sm = Mock(return_value=[])
        s = Search(Mock(search=sm))
        result = s.search("test")
        sm.assert_called_once_with("test", namespaces=[0], content=True)
        self.assertEqual(result, set())

    def test_search_unique_results(self):
        class PageDouble:
            def __init__(self, title):
                self._title = title

            def title(self):
                return self._title

            def __eq__(self, __value: object) -> bool:
                return self._title == __value.title()

            def __hash__(self) -> int:
                return 0

        rv = [
            PageDouble("a"),
            PageDouble("c"),
            PageDouble("b"),
            PageDouble("c"),
            PageDouble("a"),
        ]
        sm = Mock(return_value=rv)
        s = Search(Mock(search=sm))
        self.assertEqual({r.title() for r in s.search("test")}, {"a", "b", "c"})
