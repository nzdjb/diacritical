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
        m = Mock()
        sm = Mock()
        sm.return_value = []
        m.search = sm
        s = Search(m)
        result = s.search('test')
        sm.assert_called_once_with('test', namespaces=[0], content=True)
        self.assertEqual(result, [])
