import string
import nltk
from nltk.corpus import stopwords
from string import punctuation
#from stemming.porter2 import stem
from nltk.book import *
#from nltk.tokenize import sent_tokenize
import matplotlib.pyplot as plt
import networkx as nx
import itertools 
from itertools import combinations

def task26(b):

    length = len(b)
    
    hamming_one = []

    for i in range(length):
        
        bit_prim = b
        bit_list = list(bit_prim)
        if(bit_list[i] == "1"):
            bit_list[i] = "0"
        else:
            bit_list[i] = "1"
            
        bit_string = ''.join(bit_list)
            
        hamming_one.append(bit_string)
        
    print("B equals: " + b)
    print("Set of bitstrings with hamming distance from b = 1:")    
    print(hamming_one)
            
        
def task27(set1, set2):

    if(len(set1) == 0 and len(set2) == 0):
        print("At least one of the sets must be non-empty!")
        return 1
    else:
     
        jaccard = len(set1 & set2) / len(set1 | set2)
        
        #print("Jaccard similarity of sets:")
        #print("Set1 = ",set1)
        #print("Set2 = ",set2)
        #print("is equal " + str(jaccard))
        
        return jaccard
        
        
def task28(string1, string2):

        set1 = set(string1.split(" "))
        set2 = set(string2.split(" "))
    
        return task27(set1,set2)
        
        
def task29():

    words = [word for word in text1.tokens if len(word)<=8]
    words = set(words)
    
    result = [word for word in words if nltk.edit_distance(word,"dog") < 4 ] 
    
    print(result)
    
    #print(words[0])
   # print(nltk.edit_distance(words[0],"dog"))
        
        
def task30():

    texts = [text1.tokens,text2.tokens,text3.tokens,text4.tokens,text5.tokens,text6.tokens,text7.tokens,text8.tokens,text9.tokens]
    
    for i in range(0,len(texts)):
        for j in range(i+1,len(texts)):
            print("i="+str(i+1)+" j="+str(j+1))
            task27(set(texts[i]),set(texts[j]))
            


def hamming(s1,s2):
    result=0
    if len(s1)!=len(s2):
        return 0
    else:
        for (i,j) in enumerate(zip(s1,s2)):
            if i!=j:
                result+=1
    return result
    
def hamming2(s1,s2):
    result=0
    if len(s1)!=len(s2):
        return 0
    else:
        length = len(s1)
        for i in range(length):
            if(s1[i]!=s2[i]):
                result+=1
    return result
        
    

def task31():
    supremum = 0
      
    maxlen = 0
    for word in text1.tokens:
        if(len(word)>maxlen):
            maxlen = len(word)
            
   
    
    for i in range(1, maxlen+1):
        #print("Iteration: "+str(i))
        words = [word for word in text1.tokens if len(word) == i]
        words = list(set(words))
        #print(words)
        
        size = len(words)
        for j in range(0,size):
            if(supremum == i):
                break
            for k in range(j,size):
                if(supremum == i):
                    break
                if(hamming2(words[j],words[k]) > supremum):
                    supremum = hamming2(words[j],words[k])
                    print("Current supremum: "+ str(supremum))
                    print("Words: "+str(words[j])+"   "+str(words[k]))


           

def task32():

    data=[]
    jaccard=[]
    #size = len(text1.tokens)
    
    words = [word.lower() for word in text1.tokens if word not in punctuation]
    
    size = len(words)
    
    for i in range(0,size-1):
        if(i+1<size):
            tup = (words[i],words[i+1])
            #print(tup)
            data.append(tup)
            
    for i in range(0,size-1):
        jaccard.append(task27(set(data[i][0]),set(data[i][1])))
        
        
    #for i in range(0,size-1):
    #    print(str(data[i])+" -> "+str(jaccard[i]))
        
        
    return dict(zip(data, jaccard))
        


def help(l):

    stop = stopwords.words('english')
    wrong_words = ['."','--',',"']

    words = [word.lower() for word in text2.tokens if word not in punctuation if word not in stop if word not in wrong_words] 
    
    freq = nltk.FreqDist(words)

    filtered_word_freq = dict((word, freq) for word, freq in freq.items() if not word.isdigit() if freq >= l)
    
    return filtered_word_freq


def task33(l,s):

    G = nx.Graph()
    
    edges = []
    pair1 = []
    pair2 = []
    x = help(l)
    #for key in x:
    #    if(x[key] > 0):
    #        print(key, '->', x[key])
    
    
            
            
    for key1 in x:
        for key2 in x:
            if(key1 != key2):
               if(nltk.edit_distance(key1,key2) < s):
                   pair1.append(key1)
                   pair2.append(key2)
                   edges.append(nltk.edit_distance(key1,key2))         
            
            
            
   
    print(pair1)
    print(pair2)
    print(edges)
    
    for key in x:
        G.add_node(key)
        
    for i in range(0,len(edges)):
        
        G.add_edge(pair1[i], pair2[i],weight=edges[i])
                
    G.nodes(data=True)
    nx.draw(G, with_labels=1) 
    plt.show()   
    
    
def task34(): 

    minimal = 1000
    distances = [nltk.edit_distance(w1, w2) / len(w1 + w2) for w1, w2 in combinations(set(text2), 2)]
    min_dist = min(distances)
    print(min_dist)
    
    return [(w1,w2) for w1, w2 in combinations(set(text2), 2) if nltk.edit_distance(w1, w2) / len(w1 + w2) == min_dist]
   

def bitstrings(n):
    strings = []
    for i in range(1<<n):
        s=bin(i)[2:]
        s="0"*(n-len(s))+s
        strings.append(s)
    return strings  
        

def bitstrings2(n):

    lst = list(itertools.product([0, 1], repeat=n))
    
    bitstrings = ["".join(bitstring) for bitstring in lst] 
    
    return bitstrings

def task35(b,n):

    length = len(b)

    candidates = bitstrings(length)
   
    result = [bitstring for bitstring in candidates if hamming2(b,bitstring) == n]
   
    print(result)
    
    
def task36(s,n):

    tokens = s.split()


    print([tokens[i:i+n] for i in range(len(tokens) - n + 1)])

            

                   
                 
    
 #bag -nieunikatowo   

if __name__ == "__main__":

    
    #task26("10110")
    
    #task27(set([1,2,3,4]),set([4,5,6,7]))
    #task28("Hello there, my name is","I don't know what the problem is")
    #task29()
    #task30()
    #task31()
    #x = task32()
    #for key in x:
    #    if(x[key] > 0):
    #        print(key, '->', x[key])
   
   
    #task33(280,50)
    
    print(task34())
    
    ##  0.034482758620689655
    ##  ('acknowledgment','acknowledgments')
    
    
    #task35("00000",2)
    
    #task36("I went to Paris on my holiday. It was lovely. I saw Eiffel Tower.",4)
    
    
