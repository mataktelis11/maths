###A.M.:P19100
###Onoma:Aristotelis
###Epwnimo:Matakias
###Askisi E1 Diakrita Mathimatika Ergasia I
###PYTHON 3.8 


while True:
    try:
        a = int(input("Please enter a possitive integer: "))
        if(a>0):
            break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


"""
Tha ftia3oume to grafima Kn se morfi le3ikou 
Gia paradiegma to K5 tha einai tis morfis:
kgraph = {'1': ['2','3','4','5'],
          '2': ['1','3','4','5'],
          '3': ['1','2','4','5'],
          '4': ['1','2','3','5'],
          '5': ['1','2','3','4'],

"""



"""
arxikopoioume to lexiko:
"""

kgraph={}



"""    
Prwta ftiaxnoume mia lista pou tha periexei olous tous arithmous apo to 1 ews kai to n:
full_list=["1","2", . . . ,"n"]
"""

full_list=[]

for i in range (1,a+1):
    temp=str(i)
    full_list.append(temp)


"""
Kathe stoixeio tou lexikou ,pou einai h antistoixi korifi tou grafimatos, 
tha antistoixei se mia lista pou tha deixnei me poies korifes syndeetai 

Xreisimopoioume tin 'full_list' pou ftia3ame. Se kathe stoixeio tou grafimatos 
antistoixoume ena antigrafo tis 'full_list' kai apo autin afairoume to stoixeio sto opoio vriskomaste
dioti sto Kn kathe korifi syndeetai me oles tis ypoloipes
"""

for i in range (1,a+1):
    temp=str(i)
  
    temp_list=full_list.copy()
        
    temp_list.pop(i-1)
    
    kgraph[temp]=temp_list

del i

"""
Telos ektypwnoume stin othoni to grafima 
"""

print("Kn is :")
for z in kgraph:
    print (z,":",kgraph[z])


del z

"""
Twra elegxoume an to grafima einai grafima euler
arkei to n-1 na einai artios (vlepe askisi 1.15 i)
Pairnoume to teleutaio psifio kai koitame an einai 0 h pollaplasio tou 2
"""
x=a-1
x=str(x)
y=int(x[-1])

del x 


if (((y%2)==0)and a!=1):

    del y

    print("Yparxei kyklos euler")
    
    """
    Twra tha xrisimopoiisoume anazitisi kata vathos - DFS - me mia prosthiki:
    otan synadame symeio pou exoume episkeuthei kai den einai goneas tote vrikame kyklo

    
    Exoume tin synartisi dfs h opoioa otan tin trexoume
    vriskei enan kyklo stamataei kai vazei ton kyklo(se morfi listas) stin lista 'ALLcycles'
    """
    
        
    ##############DFS################
        
    
    def dfs(the_in,parent):
        
        
        if visited[the_in]!=True:
        
            visited[the_in]=True            
            
            cycle.append(full_list[the_in])

            for i in kgraph[full_list[the_in]]:
                
                if((visited[int(i)-1]==True) and(i!=parent)):
                    
                    cycle.append(i)                    
                
                if((i!=parent)):
                    dfs(int(i)-1,full_list[the_in])


    ###########################################    
    
    """
    Twra tha efarmosoume ton algorithmo tou Hierholzer diladi:

    3ekiname apo mia korifi
    vriskoume enan kyklo trexontas tin synartisi dfs
    meta afairoume tous komvous pou antistoixoun ston kyklo pou vrikame
    epanalamvanoume tin diadikasia mexri kanenas komvos na exei komvous

    telos tha syndiasoume olous tous kyklous pou vrikame kai tha exoume enan kyklo euler!
    
    """
    
    
    
    visited =  [False] * a
    
    ALLcycles=[]

    for initial in range(a):

        while(len(kgraph[str(initial+1)])!=0):

            visited =  [False] * a
                      
            cycle=[]
            dfs(initial,str(initial+1))
           
            count=0

            for z in range(len(cycle)):
                if cycle[z]==cycle[0]:
                    count+=1

                if count==2:
                    
                    break
            newcycle=[]
            for k in range(z+1):
                newcycle.append(cycle[k])
            
            ALLcycles.append(newcycle)


            for step in range(len(newcycle)-1):
               
                
                for g in range(len(kgraph[newcycle[step]])):
                    if(newcycle[step+1]==kgraph[newcycle[step]][g]):
                        kgraph[newcycle[step]].pop(g)
                        break
                
                for g in range(len(kgraph[newcycle[step+1]])):
                    if(newcycle[step]==kgraph[newcycle[step+1]][g]):
                        kgraph[newcycle[step+1]].pop(g)
                        break


            
    ##Svinoume metavlites kai listes pou den xreizomaste allo        
    del g
    del step
    del k
    del z
    del initial
    del newcycle
    del cycle
    del visited

    euler_circuit=[ALLcycles[0]]

    for y in range(1,len(ALLcycles)):
        if(ALLcycles[y][0]==euler_circuit[0][0]):
            euler_circuit[0].pop(-1)
            for j in ALLcycles[y]:
                euler_circuit[0].append(j)
        elif(ALLcycles[y][0] in euler_circuit[0]):
            ALLcycles[y].pop(-1)
            locate=euler_circuit[0].index(ALLcycles[y][0]) 
           
            euler_circuit[0].insert(locate,ALLcycles[y])
                     

    del ALLcycles   
    print("Euler cycle is:")
    #print(euler_circuit[0])

    print("(",end =" ")
    """
    Akolouthei kwdikas pou ektipwnei kalytera ton kyklo
    """
    
    for i in range(len(euler_circuit[0])):
        if(type(euler_circuit[0][i])==str):
            print(euler_circuit[0][i], end =" ")
        if(type(euler_circuit[0][i])==list):
            for j in euler_circuit[0][i]:
                print(j, end =" ")
        
    print(")",end =" ")  

    
else:
    print("Den yparxei kyklos euler")
