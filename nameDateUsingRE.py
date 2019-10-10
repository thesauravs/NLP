'''Write a program to extract Name and Date using regular expression from a 
    input text file'''
    
import re

file = open('nameDate.txt', 'r')

name = []
date = []

print(date)
string = str(file.readlines())
print(string)

#Regular Expression for DATES
#Assuming dates are written in MM-DD-YYYY format
date.append(re.findall('\d{2}-\d{2}-\d{4}', string))
#Assuming dates are written in DD-Mon-YYYY or DD Mon YYYY format
date.append(re.findall('\d{2}[-\s]\w{3}[-\s]\d{4}', string))
#Assuming dates are written in YYYY-MM-DD format
date.append(re.findall('\d{4}-\d{2}-\d{2}', string))

#Regular Expressions for NAMES
#re.match('Mr\.?\s([A-Z]\w*)', "Mr. Sushma")
name.append(re.findall('Mr\.?\s([A-Z]\w*)', string))
name.append(re.findall('Ms\.?\s([A-Z]\w*)', string))
name.append(re.findall('Mrs\.?\s([A-Z]\w*)', string))
print(date)
print(name)
file.close()

#test = '23-12-2009 and this is 20 jan 2009'
#haha = re.findall('\d{2}[-\s]\d{2}[-\s]\d{4}|\d{2}[-\s]\w{3}[-\s]\d{4}', test)
#print(haha)