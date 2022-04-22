import matplotlib.pyplot as plt
import numpy.random as rand

def simulation(p,N,t):

    flea_list = ["REX"]*N
    nr = flea_list.count("REX")
    na = 0
    
    with open("N{}p{}t{}.txt".format(N,p,t),"w") as out:
 
        for i in range(0,t+1):
        
            print(str(i) + " " + str(na) + " " + str(nr),file=out)
            flea = rand.randint(N)
            decision = rand.uniform()
            print(decision)
            print(str(p) + ">=" + str(decision))
            if(p >= decision):
                
                if(flea_list[flea] == "REX"):
                    flea_list[flea] = "ACE"
                    print(flea_list)
                else:

                    flea_list[flea] = "REX"
                    
                nr = flea_list.count("REX")
                na = flea_list.count("ACE")
                          
            
        out.close()
    
    
def make_graph(file):


    f = open(file,"r")
    lines = f.readlines()
    t = [int(x.split(' ')[0]) for x in lines]
    na = [int(x.split(' ')[1]) for x in lines]
    nr = [int(x.split(' ')[2]) for x in lines]
    
    #print(t)
    #print(na)
    #print(nr)
    
    plt.plot(t, na, label = "t(na)")
    plt.plot(t, nr, label = "t(nr)")
    plt.legend()
    plt.show()


 


if __name__ == "__main__":
     simulation(0.8,50,100)
     simulation(0.8,50,500)
     simulation(0.8,50,1000)
     #simulation(0.5,50,5000)
     #simulation(0.5,50,10000)
     
     make_graph("N50p0.8t100.txt")
     make_graph("N50p0.8t500.txt")
     make_graph("N50p0.8t1000.txt")
     #make_graph("N50p0.5t5000.txt")
     #make_graph("N50p0.5t10000.txt")
     
     
     
