
while True:
    try:
        a = int(input("Please enter a possitive integer: "))
        if(a>0):
            break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


print("Kn is :")
kgraph={}
full_list=[]
for i in range (1,a+1):
    temp=str(i)
    full_list.append(temp)
    




for i in range (1,a+1):
    temp=str(i)

    
  
    temp_list=full_list.copy()
    
    
    temp_list.pop(i-1)
    
    kgraph[temp]=temp_list
    
print (kgraph)


x=a-1
x=str(x)
y=int(x[-1])

if (((y%2)==0)and a!=1):












    print("artios:yparxei kyklos euler")
    ##############DFS################
    visited =  [False] * a
    #print(visited)

    #print(full_list)



    stack=[]










    ALLcycles=[]















    ##
    ##
    ##
    ##
    ##kgraph = {'1': ['2','3','4','5'],
    ##             '2': ['1','3','4','5'],
    ##             '3': ['1','2','4','5'],
    ##             '4': ['1','2','3','5'],
    ##             '5': ['1','2','3','4'],
    ##             
    ##          
    ##          
    ##          
    ##}
    ##visited =  [False] * 6
    ##stack=[]
    ##out=[]
    ##full_list=["1","2","3","4","5","6"]
    ##
    out=[]
    cycle=[]
    def dfs(the_in,parent):
        
        #print("im at:",full_list[the_in])
        #print("my parent is "+parent)
        if visited[the_in]!=True:
     
                #print("stop")

        
            visited[the_in]=True
            stack.append(full_list[the_in])
            out.append(full_list[the_in])
            #print("neighbors")
            cycle.append(full_list[the_in])
            #print(kgraph[full_list[the_in]])
            #print(visited)


            for i in kgraph[full_list[the_in]]:
                
                if((visited[int(i)-1]==True) and(i!=parent)):
                    #print("cyrcle_-----------------")
                    cycle.append(i)
                    #print(cycle)
                    
                
                if((i!=parent)):
                    dfs(int(i)-1,full_list[the_in])





    for initial in range(a):

        while(len(kgraph[str(initial+1)])!=0):

            visited =  [False] * a
            stack=[]
            
            cycle=[]
            dfs(initial,str(initial+1))

            #print(out)
            #print(cycle)
            count=0

            for z in range(len(cycle)):
                if cycle[z]==cycle[0]:
                    count+=1

                if count==2:
                    #print(z)
                    break
            newcycle=[]
            for k in range(z+1):
                newcycle.append(cycle[k])
            #print(newcycle)
            ALLcycles.append(newcycle)


            for step in range(len(newcycle)-1):
                #print(newcycle[step],newcycle[step+1])
                
                for g in range(len(kgraph[newcycle[step]])):
                    if(newcycle[step+1]==kgraph[newcycle[step]][g]):
                        kgraph[newcycle[step]].pop(g)
                        break
                
                for g in range(len(kgraph[newcycle[step+1]])):
                    if(newcycle[step]==kgraph[newcycle[step+1]][g]):
                        kgraph[newcycle[step+1]].pop(g)
                        break


            #print(kgraph)
            
    #print(ALLcycles)

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
                     
        
    print("euler cyrle is:")
    print(euler_circuit[0])



else:
    print("perittos:den yparxei kyklos euler")
