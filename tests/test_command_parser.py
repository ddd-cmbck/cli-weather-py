import unittest
from argparse import ArgumentParser, Namespace
from unittest.mock import patch

from api import CommandParser


class TestCommandParser(unittest.TestCase):  # to do

    def setUp(self) -> None:
        self.__parser = CommandParser()

    def tearDown(self) -> None:
        del self.__parser

    def test_initialization(self):
        # Test if parser and args are initialized correctly
        self.assertIsInstance(self.__parser.parser, ArgumentParser)
        self.assertIsNone(self.__parser.args)


