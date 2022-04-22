import string
import nltk
from nltk.corpus import stopwords
from string import punctuation
from stemming.porter2 import stem
from nltk.book import *
from nltk.tokenize import sent_tokenize
import re

def task16(n):

    input_sum = 0

    for i in range(n):
        x = input("Choose a number: ")
        if x.isnumeric():
            input_sum += int(x)
        else:
            return 0
            
    return input_sum

def task17(n):

    while(n>0):
        print(n)
        if n == 50 :
            break
        n-=1
    else:       
        print("Good bye!\n")
  
    
    
def task19(d,alphabet,s):

    a2 = ""
    first_char = ord(alphabet[0])
    last_char = ord(alphabet[len(alphabet)-1])

    for char in alphabet:
       
        if(ord(char) + d > last_char):
        
            a2 =  a2 + str(chr((ord(char) + d) - (last_char - first_char + 1) ))
        else:
            a2 =  a2 + str(chr((ord(char) + d)))
        
            #print(str(chr((ord(char) + d) % first_char)))



    return s.translate(str.maketrans(alphabet,a2))
    
    
def task20(book_path): 

    eng_stopwords = set(stopwords.words('english'))

    with open(book_path,"r") as book:
    
    
        words = [word.lower().replace('“', '"').replace('”', '"').translate(str.maketrans('','',punctuation)) for line in book for word in line.split()]
        
        words2 = [word for word in words if not word in eng_stopwords]
        
        words3 = [stem(word) for word in words2]
        
        counted_words = [(word, words3.count(word)) for word in set(words3)]
        
        over_hundred = list(filter(lambda word: word[1] > 99, counted_words))
        
        over_hundred.sort(key=lambda word: word[0], reverse=False)
        
        print(over_hundred)
           
    
  
def task21():

    addresses = ['8097 W. Acacia Ave. West Bloomfield, MI 48322','16 Jockey Hollow Court Windsor Mill, MD 21244', '80 Princess Drive Northbrook, IL 60062',
'29 Halifax St.Shelton, CT 06484','137 Magnolia Street Calumet City, IL 60409','28 South Winding Way Rd.Paramus, NJ 07652' ] 
    
    names = ['Darrell Sharp','Cherryl Barnett','Gracelynn Holland','Parry Everly','Jillie Kimberley','Kevin Watts']
    
    dictionary = dict(zip(names, addresses))
    
    #print(dictionary)
    
    print({name: address for name, address in sorted(dictionary.items(), key=lambda item: item[1])})
    
   
   
def task22():

    eng_stopwords = set(stopwords.words('english'))
    
    
    knight1 = [word.lower().translate(str.maketrans('','',punctuation)) for line in text6 for word in line.split()]
    knight2 = [word.lower().translate(str.maketrans('','',punctuation)) for line in text7 for word in line.split()]
    print("TASK22:")
    print("Word 'Knight' in Monty Python:")
    print(knight1.count("knight"))
    print("Word 'Knight' in Wall Street Journal:")
    print(knight2.count("knight"))
    
    words1 = set([word.lower().translate(str.maketrans('','',punctuation)) for line in text1 for word in line.split()])
    words2 = set([word.lower().translate(str.maketrans('','',punctuation)) for line in text2 for word in line.split()])
    words3 = set([word.lower().translate(str.maketrans('','',punctuation)) for line in text3 for word in line.split()])
    words4 = set([word.lower().translate(str.maketrans('','',punctuation)) for line in text4 for word in line.split()])
    words5 = set([word.lower().translate(str.maketrans('','',punctuation)) for line in text5 for word in line.split()])
    words6 = set([word.lower().translate(str.maketrans('','',punctuation)) for line in text6 for word in line.split()])
    words7 = set([word.lower().translate(str.maketrans('','',punctuation)) for line in text7 for word in line.split()])
    words8 = set([word.lower().translate(str.maketrans('','',punctuation)) for line in text8 for word in line.split()])
    words9 = set([word.lower().translate(str.maketrans('','',punctuation)) for line in text9 for word in line.split()])
    sets = [words1,words2,words3,words4,words5,words6,words7,words8,words9]
    print("TASK23:")
    print(words6.difference(words7))
    
    print("TASK24:")
    print(sets[0].intersection(*sets))
    
    
def task25():

    print("TASK25:")
    
    tokens = []
    lengths = []
    
    with open("list2-text2.txt","r") as file:
    
        data = file.read().replace('\n', '').replace('.',' . ')
        #.replace('."','@#$%^&*')
    
        sents = sent_tokenize(data)
        mx = max(sents, key=len)
        mx_fixed = mx.replace(' . ','.').replace(' .','.')
        #.replace('@#$%','."')
        print(mx_fixed)
        print(len(mx_fixed))
    
    
if __name__ == "__main__":

    #print(task16(5))
    
    #task17(15)
    #task17(54)
    #print("abbbbbbcdez changes into " + task19(5,"abcdefghijklmnopqrstuvwxyz","abbbbbbcdez"))
    #task20("list2-sherlock.txt")
    #task21()
    #task22()
    task25()
    
    
