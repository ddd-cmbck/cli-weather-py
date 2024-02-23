import unittest
from unittest.mock import patch

from formats import VerboseFormatter, DefaultFormatter, ShortFormatter, OutputFormatter


class TestFormats(unittest.TestCase):  # to do

    def setUp(self):
        output_formatter = OutputFormatter()
        verbose_formatter = VerboseFormatter()
        short_formatter = ShortFormatter()
        default_formatter = DefaultFormatter()

    def test_format(self):
        pass
