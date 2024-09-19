def kmerCounts(seq, k):
    kmerDict = {}
    for i in range(1, len(seq) -k +1):
        kmer = seq[i:i+k]
        kmerDict[kmer] = kmerDict.get(kmer, 0) + 1
    return kmerDict

seq = 'asdfdsafdsfasdfadsfdafdfafdafdsffsdffasdasdffdadfsfdsfadsafdsfadsfadsadfadsf'

print(kmerCounts(seq,3))
