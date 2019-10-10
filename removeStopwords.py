from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

#word_tokenize accepts a string as an input, not a file. 
stop_words = set(stopwords.words('english')) 
file = open("test.txt") 

line = file.read()# Use this to read file content as a stream: 
words = line.split() 
print(line)
print(words)

for r in words: 
    if not r in stop_words: 
        appendFile = open('filteredtext.txt','a') 
        appendFile.write(" "+r) 
        appendFile.close() 
