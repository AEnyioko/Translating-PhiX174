# File Descriptions:
- [ViralProt.mpfa:](https://github.com/AEnyioko/Translating-PhiX174/blob/main/ViralProt.mpfa) Protein sequences of at least 100 codons or more, organized in a fasta format
- [ViralProteome.txt:](https://github.com/AEnyioko/Translating-PhiX174/blob/main/ViralProteome.txt) All translated proteins from the genome
- [GCA_000819615.1_ViralProj14015_genomic copy.fna:](https://github.com/AEnyioko/Translating-PhiX174/blob/main/GCA_000819615.1_ViralProj14015_genomic%20copy.fna) Genome of PhiX174
- [PX174genomic.txt:](https://github.com/AEnyioko/Translating-PhiX174/blob/main/PX174genomic.txt) PhiX174 genome with original file header reomved
- [seq.py:](https://github.com/AEnyioko/Translating-PhiX174/blob/main/seq.py) Python script for translation
- [S4WYCK2H016_search_strategy.asn:](https://github.com/AEnyioko/Translating-PhiX174/blob/main/S4WYCK2H016_search_strategy.asn) Imported Blastp search
# Assignment Instructions:
In this assignment, you will need to have access to your computer (the linux environment that we just setup, maybe) to perform the analysis. The objective of this assignment is to identify hidden messages on the genome sequence of ΦX174 virus. This assignment may also require you to use a programming language. (At each step, remember GIYBF.) You can refer to the original paper Links to an external site..

Any interesting pattern that you discover will be added as bonus points. This does not have to be a novel discovery BUT you have to clearly show the steps you took in a small report.

1. Find and download the ΦX174 genome. Confirm the length of the sequence exactly as 5,386 nucleotides. If you see difference, try and found out why there is a difference.

2. Translate all the possible protein sequences (Use the genetic code table in Module 1) from the genome. Comment on how many proteins can be translated from the whole genome. You must do some filtering to decrease the meaningful protein sequences (Hint: Look at the genetic code table). This is your "putative proteome" for ΦX174 virus.

4. For the translated protein sequences in your computationally identified proteome, search each sequence online (GIYBF) to try and identify which ones are meaningful protein sequences. 

5. Now we go back to the genome. We want to count all the occurence frequencies of k-mers in the ΦX174 genome and computationally identify which k-mers are occuring more frequently than expected by random chance. For this, first create a table for all the k-mers and their counts. For example, if you set k=3, there should be counts for all 64 possible 3-mers: "AAA", "AAC", "AAG", "AAT", "ACA" ..., "TTT" in your table.

Next, start from first nucleotide of the genome, extract the 3 consecutive nucleotide sequence, then update this 3-mer's count in your count table. Next, move to the next position then update the table with the 3-mer at this position.

After all the positions on the genome are processed, you will identify whether any 3-mer is observed more than expected by chance. For this, you need to determine whether any entry of your table shows higher frequency compared to what would be observed by chance. You should think about this question: What would be the random chance that I observe "ACC"? Then compare this frequency with the frequency in your count table. Is it higher? Lower? Comment on your observations.
