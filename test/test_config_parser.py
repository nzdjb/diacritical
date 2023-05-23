from unittest import TestCase
from diacritical.config_parser import ConfigParser, Config


class TestConfigParser(TestCase):
    def test_construct_config(self):
        c = ConfigParser()
        self.assertEqual(c.config, {})

    def test_load_config(self):
        c = ConfigParser()
        c.load_config("test/config/test.toml")
        self.assertEqual(
            c.config["test"],
            Config(
                "test",
                {
                    "skip": True,
                },
            ),
        )

    def test_load_empty_config(self):
        c = ConfigParser()
        loaded = c.load_config("test/config/empty.toml")
        self.assertEqual(c.config["empty"], Config("empty"))
        self.assertEqual(c, loaded)

    def test_load_config_dir(self):
        c = ConfigParser()
        loaded = c.load_config_dir("test/config")
        self.assertCountEqual(c.config.keys(), ["test", "empty", "test2"])
        self.assertEqual(
            c.config["test"],
            Config("test", {"skip": True}),
        )
        self.assertEqual(c.config["empty"], Config("empty"))
        self.assertEqual(c, loaded)

    def test_load_config_chained(self):
        c = ConfigParser()
        c.load_config("test/config/test.toml")
        loaded = c.load_config("test/config/empty.toml")
        self.assertCountEqual(c.config.keys(), ["test", "empty"])
        self.assertEqual(
            c.config["test"],
            Config("test", {"skip": True}),
        )
        self.assertEqual(c.config["empty"], Config("empty"))
        self.assertEqual(c, loaded)


class TestConfig(TestCase):
    def test_construct_config(self):
        c = Config("Test", {})
        self.assertEqual(c.name, "Test")
        self.assertEqual(c.skip, False)
        self.assertEqual(c.ignored_pages, [])
        self.assertEqual(c.ignored_patterns, [])

    def test_construct_config_with_no_values(self):
        c = Config("Tēst")
        self.assertEqual(c.name, "Tēst")
        self.assertEqual(c.skip, False)
        self.assertEqual(c.ignored_pages, [])
        self.assertEqual(c.ignored_patterns, [])

    def test_construct_config_with_values(self):
        c = Config(
            "Tēst",
            {"skip": True, "ignored_pages": ["test"], "ignored_patterns": ["test"]},
        )
        self.assertEqual(c.name, "Tēst")
        self.assertEqual(c.skip, True)
        self.assertEqual(c.ignored_pages, ["test"])
        self.assertEqual(c.ignored_patterns, ["test"])

    def test_equality(self):
        c1 = Config("Tēst", {"skip": True, "ignored_pages": ["test"], "ignored_patterns": ["test"]})
        c2 = Config("Tēst", {"skip": True, "ignored_pages": ["test"], "ignored_patterns": ["test"]})
        self.assertEqual(c1, c2)
        c2 = Config("Test", {"skip": True, "ignored_pages": ["test"], "ignored_patterns": ["test"]})
        self.assertNotEqual(c1, c2)
        c2 = Config("Tēst", {"skip": False, "ignored_pages": ["test"], "ignored_patterns": ["test"]})
        self.assertNotEqual(c1, c2)
        c2 = Config("Tēst", {"skip": True, "ignored_pages": ["test", "test2"], "ignored_patterns": ["test"]})
        self.assertNotEqual(c1, c2)
        c2 = Config("Tēst", {"skip": True, "ignored_pages": ["test"], "ignored_patterns": ["test", "test2"]})
        self.assertNotEqual(c1, c2)
        c2 = "test"
        self.assertNotEqual(c1, c2)
