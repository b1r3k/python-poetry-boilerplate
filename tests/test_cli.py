from unittest import TestCase

from app_name import main


class TestCommandLineInterface(TestCase):
    def test_cli(self):
        with self.assertRaises(SystemExit):
            main.cli()
