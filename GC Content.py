#1/𝐿*∑𝐿 𝑖=1𝟙[𝑏𝑖∈{𝐺,𝐶}]
# calculate the fraction of G and C in a sequence
# 1.loop version
def GC_content_1(sequence):
  n_GC = 0
  for i in range(len(sequence)):
    if sequence[i] == 'G' or sequence[i] == 'C':
      n_GC +=1
  return n_GC / len(sequence) * 100
print(f"1.loop version: GC content = {GC_content_1("ACGAGTT"):.2f}%")
# 2.numpy version
import numpy as np
def GC_content_2(sequence):
  seq_array = np.array(list(sequence))
  gc_count = np.sum((seq_array == 'G') | (seq_array == 'C'))
  gc_content = gc_count / len(sequence) * 100
  return gc_content
print(f"2.numpy version: GC content = {GC_content_2("ACGAGTT"):.2f}%")
