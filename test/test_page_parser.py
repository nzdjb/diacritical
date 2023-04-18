from unittest import TestCase
from unittest.mock import Mock
from diacritical.page_parser import PageParser
from diacritical.config_parser import Config
from parameterized import parameterized


class TestPage(TestCase):
    def test_construct_page(self):
        config = Config("tēst")
        result = Mock()
        p = PageParser(config, result)
        self.assertIsInstance(p, PageParser)

    def test_candidate(self):
        config = Config("tēst")
        result = Mock()
        result.get.return_value = "test"
        p = PageParser(config, result)
        self.assertTrue(p.candidate())
        result.get.return_value = "Test"
        self.assertTrue(p.candidate())
        result.get.return_value = "Latest"  # TODO: Match only on words?
        self.assertTrue(p.candidate())

    def test_not_candidate_if_title_ignored(self):
        config = Config("tēst", {"ignored_pages": "test"})
        result = Mock()
        result.title.return_value = "test"
        p = PageParser(config, result)
        self.assertFalse(p.candidate())

    def test_page_ignored(self):
        config = Config("tēst", {"ignored_pages": "test"})
        result = Mock()
        result.title.return_value = "test"
        p = PageParser(config, result)
        self.assertTrue(p._page_ignored())
        result.title.return_value = "not_test"
        self.assertFalse(p._page_ignored())

    def test_not_candidate_if_name_not_found(self):
        config = Config("tēst")
        result = Mock()
        result.get.return_value = "something else"
        p = PageParser(config, result)
        self.assertFalse(p.candidate())

    def test_not_candidate_if_name_correct(self):
        config = Config("tēst")
        result = Mock()
        result.get.return_value = "tēst"
        p = PageParser(config, result)
        self.assertFalse(p.candidate())
        result.get.return_value = "We went to the tēst."
        self.assertFalse(p.candidate())

    def test_candidate_if_mix_of_correct(self):
        config = Config("tēst")
        result = Mock()
        result.get.return_value = "tēst test tēst"
        p = PageParser(config, result)
        self.assertTrue(p.candidate())

    def test_candidate_ignored_patterns(self):
        config = Config("tēst", {"ignored_patterns": ["latest"]})
        result = Mock()
        result.get.return_value = "latest tēst Latest"
        p = PageParser(config, result)
        self.assertFalse(p.candidate())

    @parameterized.expand(
        [
            "{{Not a typo|test}}",
            "{{not a typo|test}}",
            "{{As written|test}}",
            "{{as written|test}}",
            "{{Proper name|test}}",
            "{{proper name|test}}",
            "{{Typo|test}}",
            "{{typo|test}}",
            "{{Chem name|test}}",
            "{{chem name|test}}",
            "{{sic|test}}",
            "{{Sic|test}}",
            "{{    Not a typo   |test}}",
        ]
    )
    def test_candidate_not_a_typo(self, rv):
        config = Config("tēst")
        result = Mock()
        result.get.return_value = rv
        p = PageParser(config, result)
        self.assertFalse(p.candidate())
