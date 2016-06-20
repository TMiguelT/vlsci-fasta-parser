from Bio import SeqIO
import sys


class FastaParser:
    def __init__(self, filename):
        self.filename = filename

    # Returns a string that will be the program's output
    def parse(self):
        seq_count = 0
        seq_min = float('inf')
        seq_max = float('-inf')

        for seq in SeqIO.parse(self.filename, "fasta"):
            length = len(seq)

            seq_count += 1
            if length < seq_min:
                seq_min = length
            if length > seq_max:
                seq_max = length

        return "{}  {}  {}".format(seq_count, seq_min, seq_max)


if __name__ == '__main__':
    parser = FastaParser(sys.argv[1])
    print(parser.parse())
