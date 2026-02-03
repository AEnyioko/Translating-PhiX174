# In this assignment, you will need to have access to your computer (the linux environment that we just setup, maybe) to perform the analysis.
# The objective of this assignment is to identify hidden messages on the genome sequence of ΦX174 virus.
# This assignment may also require you to use a programming language. (At each step, remember GIYBF.) You can refer to the original paper

from Bio.Seq import Seq

def sequence(file):
    with open (file, 'r') as dna:
        s = Seq(dna.readline().rstrip())
    
    rna = s.translate()
    proteins = rna.transcribe()
    return proteins


print(sequence('PX174genomic.txt'))
