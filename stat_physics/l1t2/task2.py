import matplotlib.pyplot as plt
import random


def simulation(d,N):

    ds=[]
    

    #for i in range(d):
    #    ds.append(i)

    average_moves=[]
    
    average_moves.append(0.0)

    for i in range(1,d+1):
    
        moves=[]
    
        for j in range(N):
        
            kate=0
            john=i
            move_counter=0
            
            while True:
                
                decision1 = random.randint(0,1)         # 0 - left, 1 - right
                
                if(decision1==0):
                    kate-=1
                else:
                    kate+=1
                  
                if(kate==john):
                    move_counter+=1
                    #print("Kate: {}, John: {}".format(kate,john))
                    break
                else:
                    decision2 = random.randint(0,1)
                    
                    if(decision2==0):
                        john-=1
                    else:
                        john+=1
                        
                    move_counter+=1
                    #print("Kate: {}, John: {}".format(kate,john))
                        
                    if(kate==john):
                        break
                        
            moves.append(move_counter)
            #print("----------------------------")
            #print(move_counter)
            #print("----------------------------")
        
        average=sum(moves)/len(moves)
        #print("----------------------------")
        #print("----------------------------")
        print("{} {}".format(i,average))
        #print("----------------------------")
        #print("----------------------------")
        average_moves.append(average)
     
    #plt.plot(ds,average_moves)
    #plt.title("T_average(d) dependence")
    #plt.xlabel("d")
    #plt.ylabel("T_average")
    #plt.savefig('task2.jpg')
    #plt.show()
    #    
            
def plot():
    ys= [0.0,57.6,50.95,961.85,163.6,246.3,404.45,323.95,1951.65,64.7,1609.35,121554.9,10467.35,2488843.85,68696.1,2770.55,3073254.9,2603731.2,5741.35,41469.05,91541.5,3999.6,22413.65,456830.0,26938.1,3200446.2,41746.1,2307.6,3218.95,489572.0,5477.45,3828.5,62667.1,4453.7,197952.05,46737.85,1569476.95,2867.05,5825.55,10197.25,7710.7,6427.8,74320.2,37200.65,14549.6,220292.65,7108.05,25623.6,97353.4,442514.6,25932.95,14013.15,676108.85,222021.1,183306.45,110557.35,647819.5,65123.75,43150.25,118668.8,14290.05,14841.85,36908.05,1404345.9,400959.0,146150.1,41136.0,192494.95,59176.6,2409774.2,82136.9,37141.15,39231.0,35960.1,63429.65,52166.85,27262.1,124130.1,156313.75,374940.15,332944.75,795099.2,33808.6,16122.95,1040466.85,21371.15,34922.7,756517.3,1512893.55,60380.7,720503.8,54891.05,226914.35,897676.85,34673.4,311663.4,172498.15,734453.8,768743.1,53623.75,94359.35]
    
    ds=[]
    

    for i in range(101):
        ds.append(i)
        
    plt.plot(ds,ys)
    plt.title("T_average(d) dependence")
    plt.xlabel("d")
    plt.ylabel("T_average")
    plt.savefig('task2.jpg')
    plt.show()

if __name__ == "__main__":
     
     #simulation(100,20)
     plot()
     
     
