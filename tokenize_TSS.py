import re

#tokenize function creates a list of distinct words in corpus
#parameter for this function is the file path
#it also changes all words to lower case before creating the list

def tokenize(filename = 'test.txt'):
    with open(filename, 'r') as file:
        words = []
        all_words = []
     
        #Extract word from sentences
        for line in file:
            words += line.split()    
            #print(words)
        
        #words ending with . are processed.
        for i in range(len(words)):
            if(re.findall('w*\.', words[i])):
                words[i] = words[i][:-1]
                
        #change all words into lower case
        for i in range(len(words)):
            words[i] = words[i].lower()
        #print(words)
        
        #removing duplicate words
        for i in range(len(words)):
            if(words[i] not in all_words):
                all_words.append(words[i])
    
    return words, all_words