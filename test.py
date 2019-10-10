import tokenize_TSS as tknz
import wordFreqInFile_TSS as wf
import ngram_TSS as ng
import numpy as np

sizeOfGrams = 2
bigram = np.array(ng.ngrams('test.txt', sizeOfGrams))
print(bigram)
_, vocab = tknz.tokenize('test.txt')

#print(len(distinct_Words))

zeros = np.zeros((len(distinct_Words), len(distinct_Words)), dtype = np.int32)

for i in range(len(distinct_Words)):
    print(vocab[i])
    