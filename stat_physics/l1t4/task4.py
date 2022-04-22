import matplotlib.pyplot as plt
import numpy.random as rand
import numpy as np

def simulation(N,p,M):
    omegas = []
    edges = ["E"]*N
    balls = ["B"]*N
    
    for i in range(0,N): 
        decision = rand.uniform()     
        if(p >= decision):
            edges[i] = "M"
    
    for i in range(0,M):
        
        omega = balls.count("B") - balls.count("W")
        omegas.append(omega)
        
        #print(balls)
        #print(edges)
        #print(omega)
        
        balls = [balls[-1]] + balls[:-1]
        
        for j in range(0,N):
            if(edges[j] == "M"):
                if(balls[(j+1)%N] == "B"):
                    balls[(j+1)%N] = "W"
                else:
                    balls[(j+1)%N] = "B"
   
    
    make_graph(M,omegas)
    
    return omegas
    
    
def make_graph(M,omegas):

    mean_omega.append(omegas)
    plt.plot(list(range(0, M)), omegas, label = "omega(t)")
    #plt.show()




if __name__ == "__main__":

     

     mean_omega = []
     for i in range(0,100):
     
         mean_omega.append(simulation(500,0.009,2000))
         print(str(i+1)+"/100")
     plt.savefig("output2000.png")
     plt.show() 
     
     #print(mean_omega) 
     
     arrays = [np.array(x) for x in mean_omega]
     
     mean = [np.mean(i) for i in zip(*arrays)]
     #print(mean)
     
     plt.plot(list(range(0, len(mean))), mean, label = " mean omega(t)")
     plt.savefig("mean.png")
     plt.show()
     
     
     
     
    
     #simulation(1000,0.009,400)
     #simulation(2000,0.009,400)
 
     
     
     
