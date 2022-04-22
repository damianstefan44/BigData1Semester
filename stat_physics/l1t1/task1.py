import matplotlib.pyplot as plt
import random

def generate_random_numbers(N,a,c,m,U,task_number):

    last=1
    ys=[]
    xs=[]
    
    for i in range(N):
        xs.append(i)
    
    with open("LCG1-N{}U{}.txt".format(N,U),"w") as out:
 
 
        if(task_number != 3):
            for i in range(N):
                next=(a*last+c)%m
                last=next
                ys.append(next/m)
                print(next/m)
                print(next/m,file=out)
        else:
            for i in range(N):
               
                next=random.randint(0,m)
                ys.append(next/m)
                print(next/m)
                print(next/m,file=out)
            
        out.close()
        

    generate_plot_1(xs,ys,task_number,U,N)
    generate_plot_2(xs,ys,task_number,U,N)
    generate_plot_3(xs,ys,task_number,U,N)
    



def generate_plot_1(xs,ys,task_number,U,N):

    plt.scatter(ys,xs)
    plt.title("{}b-i".format(task_number))
    plt.xlabel("Un")
    plt.ylabel("n")
    plt.savefig('{}b-i.jpg'.format(task_number))
    plt.show()


def generate_plot_2(xs,ys,task_number,U,N):

    copy = ys.copy()
    copy.pop(0)
    ys.pop(N-1)
    
    plt.scatter(copy,ys)
  
    plt.title("{}b-ii".format(task_number))
    plt.xlabel("Un+1")
    plt.ylabel("Un")
    plt.savefig('{}b-ii.jpg'.format(task_number))
    plt.show()


def generate_plot_3(xs,ys,task_number,U,N):

    copy = ys.copy()
    copy2 = ys.copy()
    copy.pop(0)
    copy.pop(N-3)
    copy2.pop(0)
    copy2.pop(1)
    ys.pop(N-2)
    ys.pop(N-3)

    ax = plt.axes(projection='3d')
   
    ax.scatter3D(copy2, copy, ys)
    plt.savefig('{}b-iii.jpg'.format(task_number))
    plt.show()

if __name__ == "__main__":
     generate_random_numbers(1000,23,0,10**8+1,1,1) # PRNG
     #generate_random_numbers(1000,23,0,10**8+1,2,1) # PRNG
     #generate_random_numbers(1000,23,0,10**8+1,56,1) # PRNG
     #generate_random_numbers(1000,23,0,10**8+1,109,1) # PRNG
     #generate_random_numbers(1000,23,0,10**8+1,1111,1) # PRNG
     
     generate_random_numbers(1000,2**16+3,0,2**31,1,2) # RANDU
     
     generate_random_numbers(1000,23,0,10**8+1,1,3) # Mersenne Twister(Python)
     
     
     
