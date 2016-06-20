from Bio import SeqIO
import sys
from collections import defaultdict


class FastaParser:
    def __init__(self, filenames):
        self.filenames = filenames

    # Returns a string that will be the program's output
    def parse(self):

        # One large string we append our results to
        result = ""
        for filename in self.filenames:
            result += filename + '\n'

            # Variables
            seq_count = 0
            seq_min = float('inf')
            seq_max = float('-inf')
            counts = defaultdict(int)

            # Parsing
            for seq in SeqIO.parse(filename, "fasta"):
                # Update the count
                seq_count += 1

                # Update length-based metrics
                length = len(seq)
                if length < seq_min:
                    seq_min = length
                if length > seq_max:
                    seq_max = length

                # Update frequency-based metrics
                for char in seq:
                    counts[char] += 1

            # Appending the string
            result += "{}\t{}\t{}\n".format(seq_count, seq_min, seq_max)
            for key in sorted(counts.keys()):
                result += "{}\t{}\n".format(key, counts[key])

        return result


if __name__ == '__main__':
    parser = FastaParser(sys.argv[1:])
    print(parser.parse())
