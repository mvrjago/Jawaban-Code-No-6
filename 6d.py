from Bio.Seq import Seq
import matplotlib.pyplot as plt

seq = Seq('GACAAGGACCTGCCACGGTGGAACTTCACCGACTTCATGCACTCGTTCATGATCGTGTTCCGGGTGCTGTGCGGCGAGTGGATCGAATCCATGTGGGACTGCATGCTGGTCGGCGACGTGTCCTGCATTCCGTTCTTTTTGGCCACCGTAGTGATAGGAAATCTAGTAGTAAGTATCCCCTTTCGGTCCAGCAAGCAGTGCTGCGTGAACAACGGATCGTACTAATCGGAGAATGCTTTCTCTCCCCCTTCCAATCCAGGTACTTAACCTTTTCTTAGCCTTGCTTTTGTCCAATTTCGGTTCATCGTCGCTGTCGGCACCGACGGCCGACAACGAAACG')

def gc_skew(seq, window = 1000):
      skews = []
      skews2 = []
      for i in range(0,len(seq), window):
        subseq = seq1[i:i+window]
        g_count = subseq.count('G')
        c_count = subseq.count('C')
        a_count = subseq.count('A')
        t_count = subseq.count('T')
        if g_count + c_count != 0:
            skew = (g_count-c_count)/(g_count+c_count)
            skews.append(skew)
        else:
            skews.append(0)
        if a_count + t_count != 0:
            skew1 = (a_count-t_count)/(a_count+t_count)
            skews2.append(skew1)
        else:
            skews2.append(0)
      
      return skews,skews2

GC,AT = gc_skew(seq,window = 10)
plt.plot(GC)
plt.show()
plt.plot(AT)
plt.show()
