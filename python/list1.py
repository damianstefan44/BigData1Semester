import math

def task3_1():
    X = [-1,0,1]
    Y = [-1,0,1]
    Z = [-1,0,1]
    p = 1/(len(X)*len(Y)*len(Z))
    lengths = []

    for x in X:
        for y in Y:
            for z in Z:
                lengths.append(math.sqrt(math.pow(x,2)+math.pow(y,2)+math.pow(z,2)))
    expected = 0
    variance = 0
    
    for e in lengths:
        expected += e*p
    print("Expected value is: " + str(expected))
    
    for e in lengths:
        variance += math.pow((e-expected),2)
    variance/=len(lengths)
    print("Variance is: " + str(variance))

if __name__ == "__main__":
    task3_1()









import random
from numpy import dot
from numpy.linalg import norm
from itertools import combinations


def task1():
    x = input("Choose an integer: ")
    if x.isdigit():
        y = int(x)
        #print(y)
        if(y%2 == 0):
            print("The number is even")
        else:
            print("The number is odd")
    else:
        print("Input is not an integer")


def task2():

    list = []

    for i in range(20):
        x = random.randint(10,99)
        list.append(x)

    print("The mean value is: " + str(sum(list)/len(list)))
    print("The max value is: " + str(max(list)))

def task3():
    vector1 = []
    vector2 = []
    d = int(input("Choose integer d: "))

    print("Choose d values for vector1:")
    for i in range(d):
        v1 = float(input())
        vector1.append(v1)
    print("Choose d values for vector2:")
    for i in range(d):
        v2 = float(input())
        vector2.append(v2)

    result = dot(vector1, vector2) / (norm(vector1) * norm(vector2))
    print("Cosine of the angle between vector1 and vector2 = " + str(result))


def task4(a,b,c):
    for i in range(a+1,b):
        if i%c == 0:
            print(i)

def task5(list1,list2):
    common = []
    for element in list1:
        if(element in list2):
            common.append(element)
    print(common)

def task6(x):
    x_changed = x.replace('a','')
    print(x + " turns into: "+x_changed)

def task7(sentence):
    letters = 0
    digits = 0

    for c in sentence:
        if(c.isalpha()):
            letters+=1
        elif(c.isdigit()):
            digits+=1

    print("Sentence: " + sentence)
    print("has: " + str(letters) + " letters and " + str(digits) + " digits")


def task8(set):
    l = len(set)
    for i in range(0,l+1):
        
        for k in combinations(set,i):
            print("{" + ','.join(k) + "}")
            

def task9(string):
    mx = -1
    for c in set(string):
        q = string.count(c)
        if(q>mx):
            mx = q
            
    for c in set(string):
        q = string.count(c)
        if(q == mx):
            print("Most frequent letter in string is: " + c + " Frequency: " + str(mx))
         
def task10(number):
    print(str(bin(number))[2:])
    
def task11(list):
    res = [e for e in list if e>=0]
    print(res)
    
def task12(list):
    res = [e for e in list if len(e)<6]
    print(res)
    
def task13(set):
    set_list = list(set)
    list1 = [len(e) for e in set_list]
    mx = max(list1)
    matches = [e for e in list1 if e == mx]
    matches = [i for i in range(len(list1)) if list1[i] == mx]
    res = [set_list[e] for e in matches]
    print(res)
    
def task14(list1,list2):
    res = []
    length = len(list1)
    for i in range(length):
        res.append(list1[i])
        res.append(list2[i])
    print(res)
    
def task15(list):
    integers = []
    strings = []
    for e in list:
        if(isinstance(e, int)):
            integers.append(e)
        else:
            strings.append(e)
    integers.sort()
    strings.sort
    result = strings + integers
    print(result)
    

def main():

    #task1()
    #task2()
    #task3()
    #task4(2,16,2)
    #task5([1,2,3,4,5,6],[5,6,7])
    #task6("abracadabra")
    #task7("Ala1 ma2 kota3")
    #task8({"a", "b", "c", "d"})
    #task9("aaabbbcccd")
    #task10(8)
    #task11([0,-1,1,-2,2,-9,3,-56,4,-100,5])
    #task12(["sfasfasfasf","12345","123456","abcde","abcdef"])
    #task13({"asf","abc1","ab","51g","a","aba"})
    #task14(["a1","a2","a3"],["b1","b2","b3"])
    task15(["a",4,"ab","ac",3,1,2,"aaa","bc"])
    
    
if __name__ == "__main__":
    main()
