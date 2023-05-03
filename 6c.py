from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
from Bio.SeqUtils import MeltingTemp as mt
from Bio.SeqUtils import molecular_weight

seq = Seq('GACAAGGACCTGCCACGGTGGAACTTCACCGACTTCATGCACTCGTTCATGATCGTGTTCCGGGTGCTGTGCGGCGAGTGGATCGAATCCATGTGGGACTGCATGCTGGTCGGCGACGTGTCCTGCATTCCGTTCTTTTTGGCCACCGTAGTGATAGGAAATCTAGTAGTAAGTATCCCCTTTCGGTCCAGCAAGCAGTGCTGCGTGAACAACGGATCGTACTAATCGGAGAATGCTTTCTCTCCCCCTTCCAATCCAGGTACTTAACCTTTTCTTAGCCTTGCTTTTGTCCAATTTCGGTTCATCGTCGCTGTCGGCACCGACGGCCGACAACGAAACG')

gc_content = gc_fraction(seq)*100
melting_temperature = mt.Tm_GC(seq)
bobot_molekul = molecular_weight(seq)

print("Hasil Hitungan GC Content, Melting Temperature dan Molecul Weight")
print("==================================================================")
print ("GC Content :",gc_content)
print ("Melting Temperature :",melting_temperature)
print ("Molecular Weight :",bobot_molekul)