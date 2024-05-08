
#start of exam 4 

#import 
import sys

#define k-mer
def find_kmers(sequence, k):
  kmers = {}
  #loop sequences 
  for i in range(len(sequence) - k):
    kmer = sequence[i+1:i+1+k]
    next_kmer = sequence[i+1:i+1+k]
    if kmer not in kmers:
      kmers[kmer] = set()
      kmers[kmer].add(next_kmer)
  #return all containing kmers
  return kmers 

#collect data
def process_sequences(sequences, k):
  all_kmers = {}
  for sequence in sequences:
    kmers = find_kmers(sequence, k)
  return all_kmers



