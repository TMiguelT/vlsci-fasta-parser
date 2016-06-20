from Bio import SeqIO
import sys


class FastaParser:
    def __init__(self, filename):
        self.filename = filename

    # Returns a string that will be the program's output
    def parse(self):
        i = 0
        for seq in SeqIO.parse(self.filename, "fasta"):
            i += 1
        return str(i)


if __name__ == '__main__':
    parser = FastaParser(sys.argv[1])
    print(parser.parse())
