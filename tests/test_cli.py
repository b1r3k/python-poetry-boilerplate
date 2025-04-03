from unittest import TestCase

from app_name import main


class TestCommandLineInterface(TestCase):
    def test_cli(self):
        with self.assertRaises(SystemExit):
            main.cli()


class TestEnvironmentVariables(TestCase):
    def test_environment_variables(self):
        self.assertEqual(main.settings.APP_NAME, "app_name")
