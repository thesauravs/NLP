import tokenize_TSS as tknz

def wordCount(filename = 'test.txt'):
    words, all_words = tknz.tokenize(filename)
            
    #initializing the count of respective words
    count = [0]* len(all_words)
    #increasing the count as the word is encountered in 'words' list
    for i in range(len(all_words)):
        for j in range(len(words)):
            if(words[j] == all_words[i]):
                count[i] += 1
    #to make dict
    wordFreq = dict(zip(all_words, count))
    
    #print(words)        
    #print(all_words)
    #print(count)
    #print(len(all_words))
    #print(len(count))
    #print(wordFreq)
    #file.close()
    return wordFreq
