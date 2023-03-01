from unittest import TestCase
from diacritical.config import Config

class TestConfig(TestCase):
    def test_construct_config(self):
        c = Config()
        self.assertEqual(c.config, {})

    def test_load_config(self):
        c = Config()
        c.load_config('test/config/test.toml')
        self.assertEqual(c.config['test'], {
            "skip": True,
        })

    def test_load_empty_config(self):
        c = Config()
        c.load_config('test/config/empty.toml')
        self.assertEqual(c.config['empty'], {})
    
    def test_load_config_dir(self):
        c = Config()
        c.load_config_dir('test/config')
        self.assertCountEqual(c.config.keys(), ['test', 'empty'])
        self.assertEqual(c.config['test'], {
            "skip": True,
        })
        self.assertEqual(c.config['empty'], {})
