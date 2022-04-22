import matplotlib.pyplot as plt
import numpy as np
import scipy.special as spec
import math


def make_plot(krange,nrange, omega_lambda):

    ks = np.linspace(1,krange)
    ns = np.linspace(1,nrange)
    
    
    
    for n in range(1,nrange):  #S(n)
    
        plt.plot(ks,omega_lambda(n,ks))
    
    plt.show()
    
    for k in range(1,krange):  #S(k)
    
        plt.plot(ns,omega_lambda(ns,k))
    
    plt.show()
    
def make_plot2(nrange,n1range):

        
    mm = list(np.arange(-nrange,nrange,2))
    
    # omega = N choose N1 = N!/(((M+N)/2)! * ((N-M)/2)!)

    
    plt.plot(mm,[np.log(math.factorial(nrange)/(math.factorial(int((nrange-x)/2))*math.factorial(int((x+nrange)/2))),where=math.factorial(nrange)) for x in mm ])  
    
    plt.plot(mm,[2*x-nrange for x in mm]) 
    
    plt.show() 
        
   
    #APPROXIMATED
    
    #plt.plot(mm,[nrange*np.log(nrange) + (x-nrange)*np.log(nrange-x) - x*np.log(x) for x in mm ])  
    
    plt.plot(mm,[nrange*np.log(nrange) - nrange - ((x+nrange)/2)*np.log((nrange+x)/2) + (x+nrange)/2 - ((nrange-x)/2)*np.log((nrange-x)/2) + (nrange-x)/2 for x in mm ])  
    
    plt.plot(mm,[2*x-nrange for x in mm])  
    
     
    plt.show()
    




def t1(krange,nrange):

    task1 = lambda n,k: n * np.log(k)
    
    make_plot(krange,nrange,task1)



def t2(krange,nrange):

    task2 = lambda n,k: np.log(spec.comb((n+k-1),n))
    
    make_plot(krange,nrange,task2)


def t3(krange,nrange):

    task3 = lambda n,k: np.log(spec.comb(k,n),where=spec.comb(k,n)>0)
    
    make_plot(krange,nrange,task3)
    
def t5(nrange,n1range):

    task5 = lambda n1,n: np.log(spec.comb(n,n1),where=spec.comb(n,n1)>0)
    
    
    make_plot(nrange,n1range,task5)    
    
# omega = (N choose N') * ((N-N') choose N')    

def t6(nrange,n1range):

    task6 = lambda n1,n: np.log(spec.comb(n,n1)*spec.comb(n-n1,n1),where=(spec.comb(n-n1,n1)>0))
    
    
    make_plot(nrange,n1range,task6)    



def t7(nrange,n1range):

    make_plot2(nrange,n1range)  
    

if __name__ == "__main__":
    #task1(100,50)
    #task2(100,50)
    #task3(20,20) = #task5(20,20)
    #task5(100,50)
    #task6(100,50)
    
    #t1(100,50)
    #t2(100,50)
    t3(100,50)
    #t5(100,50)
    #t6(100,50)
    #t7(100,50)
    


# S = kb ln(omega)    omega - all distinguishable states

#################  1 

#k distinguishable dogs
#N distinguishable fleas

#omega = k^N

#S = ln k^N = N*ln(k) calculate S(n) and S(k)     different k's or N's on same plot



#################  2

#k distinguishable dogs
#N indistinguishable fleas

#omega = N + k - 1 choose N

#S = ln(omega)

#################  3

#k distinguishable dogs
#N indistinguishable fleas
#at most 1 flea on a dog

#k>= N

#omega = k choose N

#################  5

#N beads
#N1 black, N2 = N-N1 - white

# omega = N choose N1


#################  6

#N beads
#N' red, N' blue, N-2*N' - white

# omega = (N choose N') * ((N-N') choose N')


################  7

# N particles:
# 1 state: E0            N1 particles
# 2 state: -E0           N2 = N -N1 particles

# E = ME0    - M constant

# M E0 = (N1-N+N1)* E0
# M = 2N1 -N
# N1 = (N+M)/2
# N2 = N-N1 = (N-M)/2

# omega = N choose N1 = N!/(((M+N)/2)! * ((N-M)/2)!)


# find max
# ds/dM = 0


# stirling approximation

# ln(n!) =?= n * ln(n) - n



# ds/dM = 0 =>  huge equation ==> N - M = M + N ==> M = 0



# PLOT EXACT VALUES AS WELL AS APPROXIMATED TO SEE
