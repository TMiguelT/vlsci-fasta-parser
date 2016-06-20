import unittest
from fasta import FastaParser


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = FastaParser('two_sequences.fasta')

    def test_output(self):
        assert(self.parser.parse() == '2\t7\t14')
