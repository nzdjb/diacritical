from unittest import TestCase
from diacritical.config_parser import ConfigParser


class TestConfigParser(TestCase):
    def test_construct_config(self):
        c = ConfigParser()
        self.assertEqual(c.config, {})

    def test_load_config(self):
        c = ConfigParser()
        c.load_config("test/config/test.toml")
        self.assertEqual(
            c.config["test"],
            {
                "skip": True,
            },
        )

    def test_load_empty_config(self):
        c = ConfigParser()
        loaded = c.load_config("test/config/empty.toml")
        self.assertEqual(c.config["empty"], {})
        self.assertEqual(c, loaded)

    def test_load_config_dir(self):
        c = ConfigParser()
        loaded = c.load_config_dir("test/config")
        self.assertCountEqual(c.config.keys(), ["test", "empty"])
        self.assertEqual(
            c.config["test"],
            {
                "skip": True,
            },
        )
        self.assertEqual(c.config["empty"], {})
        self.assertEqual(c, loaded)

    def test_load_config_chained(self):
        c = ConfigParser()
        c.load_config("test/config/test.toml")
        loaded = c.load_config("test/config/empty.toml")
        self.assertCountEqual(c.config.keys(), ["test", "empty"])
        self.assertEqual(
            c.config["test"],
            {
                "skip": True,
            },
        )
        self.assertEqual(c.config["empty"], {})
        self.assertEqual(c, loaded)


class TestConfig(TestCase):
    def test_construct_config(self):
        pass
