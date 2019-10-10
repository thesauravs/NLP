#ngrams takes two parameters list of tokens and number of grams
#default values result in bigram of "This is a test file"
import tokenize_TSS as tknz

def ngrams(filename = 'test.txt', sizeOfGrams = 2):
    _, tokens = tknz.tokenize(filename)
    ngrams = []
    for i in range(sizeOfGrams):
       ngrams.append(tokens[i:])
        
    ngrams = list(zip(*ngrams))
    return ngrams