run = 1                     # Initialize run
all_fire = []               # all fire empty list
while run <= 6:             # while loop for simulation run. eg. here number of runs is less than equal to 20
    print("#####Component Rail Crack#####")
    P = ['A', 'B','C','D','E','F','G','H','I','J']
    T = ['t1','t2','t3','t4','t5','t6','t7','t8','t9','t10','t11']
    print("Run number:" + str(run))
    GC1 = 0.0
    life1 = 70.00              #life-time of the component in days
    M = [1,0,0,0,1,0,0,0,1,0]     #Initilize marking
    combine = []   #Empty list for fired transitions and there time of firing. Both will be stored as tuple
    LCLOCK = []
    fire = []
    while GC1 <= life1:       #while loop for Global Clock        
 #########Condition of enabling transitions. Put enabled transitions in empty list E########
        import random
        E =[]   
        if M[0] == 1:
            E.append(T[0])
            
        probs = [0.70,0.30]   ##index 0 is t2 and index 1 is t3
        r = random.random()
        index = 0
        while(r >= 0 and index < len(probs)):
          r -= probs[index]
          index += 1
        index_t = index-1
            
        if index_t == 0 and M[1]==1:
            E.append(T[1])
        if index_t == 1 and M[1]==1:
            E.append(T[2]) 
        if M[4] == 1:
            E.append(T[3])
        if M[1] == 1 and M[5]==1:
            E.append(T[4])
            
        probs = [0.30,0.70]   ##index 0 is t6 and index 1 is t7
        r = random.random()
        index = 0
        while(r >= 0 and index < len(probs)):
          r -= probs[index]
          index += 1
        index_t = index-1
            
        if index_t == 1 and M[2] == 1 and M[5] == 1:
            E.append(T[5])
        if index_t == 0 and M[3]==1 and M[5] == 1:
            E.append(T[6])
        if M[6] == 1:
            E.append(T[7])
        if M[7] == 1:
            E.append(T[8]) 
        if M[8] == 1:
            E.append(T[9])
        if M[9] == 1:
            E.append(T[10])    
        
#################Find firing time FT of enabled transitions#####################
        FT = []
        import math
        rand = random.random()
        if 't1' in E:
            FT.append(0)
        if 't2' in E:
            FT.append(random.weibullvariate(9, 6))
        if 't3' in E:
            FT.append(random.weibullvariate(9, 6))
        if 't4' in E:
            FT.append(3)
        if 't5' in E:
            FT.append(0)
        if 't6' in E:
            FT.append(4)
        if 't7' in E:
            FT.append(4)
        if 't8' in E:
            FT.append(2)
        if 't9' in E:
            FT.append(2)  
        if 't10' in E:
            FT.append(68)
        if 't11' in E:
            FT.append(3)    
          
 ##########Update marking. And add fire transition and its local time to fire in empty list 'fire'###################
        LC = min(FT)       #local clock is set
        LCLOCK.append(LC)
        Transition_fire = E[FT.index(min(FT))]   # which transition will fire. first find minimum of FT then, its index to retrive enabled transition to be fired from E.
        fire.append(Transition_fire)
        T.index(Transition_fire)   #find the transition index from T to find the Ind matrix list to substracted
        Ind_remove = [[-1,0,0,0,0,0,0,0,0,0],[0,-1,0,0,0,0,0,0,0,0],[0,-1,0,0,0,0,0,0,0,0],[0,0,0,0,-1,0,0,0,0,0],[0,-1,0,0,0,-1,0,0,0,0],[0,0,-1,0,0,-1,0,0,0,0],[0,0,0,-1,0,-1,0,0,0,0],[0,0,0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,-1,0,0],[0,0,0,0,0,0,0,0,-1,0],[0,0,0,0,0,0,0,0,0,-1]]
        Ind_add = [[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,1,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,1,0,1,0,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1,0]]
        M = [a + b + c for a, b, c in zip(M,Ind_remove[T.index(Transition_fire)],Ind_add[T.index(Transition_fire)])]    #[a + b for a, b in zip(list1, list2)] add two numbers in a list
        GC1 = GC1 + LC       # Global clock is updated by adding the local clock time in it
        combine = [list(a) for a in zip(fire, LCLOCK)]  
        LC = 0.0   ##reset local clock
#######Result Collection#######
    print("Fire list is: " + str(combine))         #print Fire tuple list
    all_fire.append(combine)
    run = run + 1
import pandas
df = pandas.DataFrame(all_fire)  ##convert to dataframe
print(all_fire)      ###print 'all_fire' list which contain 'fire' list  for all components## 
print("dataframe is:" + str(df))
df.to_csv('output1.csv')