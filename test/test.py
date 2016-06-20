import unittest
from fasta import FastaParser
import os.path

__dir__ = os.path.dirname(__file__)


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(__dir__, './expected.txt')) as expect_file:
            self.parser = FastaParser(['two_sequences.fasta', 'one_sequence.fasta'])
            self.expected = expect_file.read()

    def test_output(self):
        assert(self.parser.parse() == self.expected)
