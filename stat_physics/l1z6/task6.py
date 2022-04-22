import matplotlib.pyplot as plt
import numpy as np
import scipy.special as spec
import math
from scipy.stats import linregress


def task1(k):

    repetitions = 1

    pi_values = []

    for i in range(1,k+1):
        print("I'm in loop: "+str(i))
    
        n=pow(10,i)
        
        pi_sum = 0
    
        for j in range(0,repetitions):
            print("  I'm in repetition number: "+str(j))
            in_circle = 0
            
            
            for a in range(0,n):
                print("    I'm in point number: "+str(a))
                x = np.random.uniform(-1,1)
                y = np.random.uniform(-1,1)
                
                if(pow(x,2) + pow(y,2) <= 1):
                    in_circle+=1
                    #print("in circle")
             
            pi_prime = 4*in_circle/n
            pi_difference = abs(math.pi - pi_prime) 
            pi_sum += pi_difference
        pi_mean = pi_sum/repetitions
        print(pi_mean)
        pi_values.append(pi_mean) 
    
    return pi_values
         
def plot1():
   pi_values = task1(7)
   xs = [pow(10,x) for x in range(1,8)]
   ys = [x for x in pi_values] 
   
   logxs = [np.log(pow(10,x)) for x in range(1,8)] 
   logys = [np.log(x) for x in pi_values] 
   
   reg = linregress(logxs, logys)
   print(reg)
 
   plt.axline(xy1=(0, reg.intercept), slope=reg.slope, linestyle="--", color="k")    
   plt.plot(logxs,logys) 
  
   plt.xlabel("n")
   plt.ylabel("absolute error")
   #plt.xscale("log")
   #plt.yscale("log")
   plt.savefig('1.png')
   plt.show()
   
   
   
   
def task2(k):


    coin = ['H', 'T']
    
    odd_number_heads=0
    three_heads=0
    
    for j in range(k):
    
        output = np.random.choice(coin, 3, p=[0.5, 0.5])   
        count = np.count_nonzero(output == 'H')
        if(count == 1):
            odd_number_heads+=1
        elif(count == 3):
            odd_number_heads+=1
            three_heads+=1
            
     
    return three_heads/odd_number_heads 
    
    
def task3(k):


    average=0
    
    for i in range(k):
    
        fixed_points=0
        perm = np.random.permutation(100)
        
        for j in range(len(perm)):
            if perm[j] == j:
                fixed_points+=1
                
        average+=fixed_points
        
    return average/k
                

def task3b(k):

    fixed_points_two=0
    
    for i in range(k):
    
        fixed_points=0
        perm = np.random.permutation(100)
        
        for j in range(len(perm)):
            if perm[j] == j:
                fixed_points+=1
                
        if(fixed_points == 2):
            fixed_points_two+=1
        
    return fixed_points_two/k        
      

def task4(k,rolls):


    dice = ['1', '2', '3', '4', '5', '6']
    
    no_number_twice=0
    
    for j in range(k):
    
        output = np.random.choice(dice, rolls, p=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]) 
          
        count1 = np.count_nonzero(output == '1')
        count2 = np.count_nonzero(output == '2')
        count3 = np.count_nonzero(output == '3')
        count4 = np.count_nonzero(output == '4')
        count5 = np.count_nonzero(output == '5')
        count6 = np.count_nonzero(output == '6')
        
        if(count1!=2 and count2!=2 and count3!=2 and count4!=2 and count5!=2 and count6!=2):
            no_number_twice+=1
        
     
    return no_number_twice/k
    
      


if __name__ == "__main__":
    #plot1()
    #print(task2(1000000))    # 0.24966240479815308 ~ 0.25 = 1/4
    #print(task3(100000))     # 1.00347 ~ 1
    #print(task3b(1000000))   # 0.183384 
    print(task4(100000,5))    # 0.26597
    print(task4(100000,10))   # 0.12936

    








#################### 1



#estimate value of pi


#we check how many generated points are in circle of radius r=1

#we make a square and circle in it
#S_circle/ S_square = pi/4


#x,y from uniform distribution[-1,1]

#P{x^2 + y^2} = pi/4


#I = {1 if x^2 + y^2 <=1
#     0 therwise}
     
#E(I) = 1*P{x^2 + y^2 <=1} + 0*P{otherwise} = 1*P{x^2 + y^2 <=1}

#law of large numbers

#Ii - iid, 

#I_dash = I1+I2+....+In / n ---> E(I)

#pi_prime = 4*I_dash


#1. define function pi-approx(N)
#2. initialize counter(how many inside)
#3. for each generate x,y from uniform distribution
#4. return counter/n * 4



#how accuracy changes when number of points is changed

#plot on log log scale x=N=number of points, y= math.pi - pi_prime, check linear regression


##################### 3

# random permutation




