# In this assignment, you will need to have access to your computer (the linux environment that we just setup, maybe) to perform the analysis.
# The objective of this assignment is to identify hidden messages on the genome sequence of ΦX174 virus.
# This assignment may also require you to use a programming language. (At each step, remember GIYBF.) You can refer to the original paper

import importlib.util
import os
from Bio.Seq import Seq

# locate ORF.py relative to this file and load the module
# https://github.com/AEnyioko/Rosalind/blob/main/BioinfoStronghold/questions/ORF.py
here = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.abspath(os.path.join(here, '..', 'Rosalind', 'BioinfoStronghold', 'questions', 'ORF.py'))
spec = importlib.util.spec_from_file_location('orf_module', file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
open_reading_frames = module.open_reading_frames

# function to read in genome sequence from file
def sequence(file):
    with open (file, 'r') as dna:
        s = Seq("".join(dna.readlines()).rstrip())
    return s

genome_path = os.path.join(here, 'PX174genomic.txt')
seq = sequence(genome_path)

# write protein sequences of length at least 100 to output file
with open('ViralProt.mpfa', 'w') as prot:
    count = 0
    for i in open_reading_frames(genome_path):
        if len(i) >= 100:
            count += 1
            prot.write(">SEQUENCE_" + str(count) + '\n' + i + '\n')

# write sequences in proteome to file
with open('ViralProteome.txt', 'w') as proteome:
    for protein in open_reading_frames(genome_path):
        proteome.write(protein + '\n')

# finding k-mers
def kmers(sequence, k):

    kmers_list = []
    for i in range(len(sequence) - k + 1):
        kmer = (sequence[i:i+k])
        if len(kmer) == k and '\n' not in str(kmer):
            kmers_list.append(str(kmer))
    
    kmer_freq = {}
    for kmer in kmers_list:
        if kmer in kmer_freq:
            kmer_freq[kmer] += 1
        else:
            kmer_freq[kmer] = 1
    return dict(sorted(kmer_freq.items(), key=lambda x: x[1], reverse=True))

print("There are " + str(len(kmers(seq, 3))) + " possible codons" + '\n' + "The codon frequencies are as follows:\n" )
print(kmers(seq, 3))
