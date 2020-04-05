permutation={}
index=1

while True:
    check=True
    try:
        a=input("Give a permutation:")
        
        a= a.split(" ")
      



        for i in a:
            if i ==(''):
                continue
            temp = int(i)
            if (temp>0):
                    
                permutation[index]=temp
                index += 1
            else:
                print("TYPED invalid:Only possitive integers")
                check=False
                break
        if(check!=False):        
            break
    except ValueError:
        print("TYPED invalid:Only numbers and spaces")
        


del index,temp




def checkpermutation(permutation):

    for i in permutation:
        if permutation[i]>len(permutation):
            print("this is not a permutation")
            return False

    for i in permutation:
        s=0
        for j in permutation:

            if permutation[i]==permutation[j]:
                s+=1
                if s==2:

                    print("this is not a permutation")
                    return False
                    

    return True


def numberswitcher(n):
    numberswitcher=True
    for i in range(1,n+1):
        if numberswitcher==True:
            numberswitcher=False
        else:
            numberswitcher=True
    return numberswitcher
        




def printpermutation(permutation,Iperm):

    
    print("Permutation is:")
    print("m =(",end=" ")
    for i in range(1,len(permutation)+1):
        print(permutation[i],end=" ")
        if(i!=permutation[i]):
            Iperm=False 
    print(")")

    
    if(Iperm==True):
        print("ideal permutation!")
    print("Lenght of permutation is:",len(permutation))

    return Iperm

def oppositeofpermutation(permutation):

    print("Opposite of permutation is:")
    print("m^(-1) =(",end=" ")

    
    for i in range(1,len(permutation)+1):
        for j in range(1,len(permutation)+1):
            if(permutation[j]==i):
                print(j,end=" ")       
    print(")")

def countercycles(AllCycles,Iperm,CounterCycles):
    if(len(permutation)<2):
        print("Cannot be expressed with counter cycles")
    else:
        
        if (Iperm==False):
            
            
            for i in reversed(AllCycles):
        
                if len(i)==1:
                    AllCycles.pop(AllCycles.index(i))
                
        
            element=[]
            
            for i in (range(len(AllCycles))):
                if (len(AllCycles[i]))==2:
                    CounterCycles.append(AllCycles[i])        
                    
                else:
                    
                    
                    for j in range(1,len(AllCycles[i])):
                        element.append(AllCycles[i][0])
                        element.append(AllCycles[i][-1])
                        CounterCycles.append(element)
                        AllCycles[i].pop()
                        element=[]
                        
        else:
           CounterCycles=[[1,2],[1,2]] 


        print("Permutation in counter-cycles:")
        print("m =",end=" ")
        for i in range (len(CounterCycles)):
            print("(",end=" ")
            for j in range(len(CounterCycles[i])):
                print(CounterCycles[i][j],end=" ")
            print(")",end=" ")

        print()
        if (numberswitcher(len(CounterCycles))==False):
            print("sgn(m)=-1 peritti")
        else:
            print("sgn(m)=1 artia")


   
                




def findcycles(permutation):

    permutationlen=len(permutation)

    incycle=[False]*permutationlen



    def adder():

       while True:

            if(permutation[cycle[-1]]!=cycle[0]):
                incycle[cycle[-1]-1]=True
                cycle.append(permutation[cycle[-1]])
            else:
                incycle[cycle[-1]-1]=True
                break



    def newlist(cycle):

        for i in range(1,permutationlen+1):        
            

            if (i==permutationlen)and(incycle[-1]==True):
            
     
                cycle=[]
                
                return cycle
                    
            elif(incycle[i-1]==False):

                cycle=[i]
                return cycle
            else:
                continue
                    
    cycle=[]

    cycle.append(1)



    while True:

        adder()

        AllCycles.append(cycle)

        cycle=newlist(cycle)

        if(len(cycle)==0):
            break

        
    del cycle
    #print(AllCycles)



def printallcycles():

    print("Permutation in cycles:")
    print("m =",end=" ")
    
    for i in range (len(AllCycles)):
        
        print("(",end=" ")
        for j in range(len(AllCycles[i])):
            print(AllCycles[i][j],end=" ")
        print(")",end=" ")

    print()



def printstrangecycles():

    print("Permutation in strange cycles:")
    print("m =",end=" ")
    
    for i in range (len(AllCycles)):
        if(len(AllCycles[i])==1):
            continue
        print("(",end=" ")
        for j in range(len(AllCycles[i])):
            print(AllCycles[i][j],end=" ")
        print(")",end=" ")

    print()




if(checkpermutation(permutation)==True):
    

    AllCycles=[]
    CounterCycles=[]
    Iperm=True




    Iperm=printpermutation(permutation,Iperm)

    oppositeofpermutation(permutation)

    findcycles(permutation)

    if(Iperm==False) and (len(AllCycles)>1):
        printallcycles()
        printstrangecycles()
    else:
        printallcycles()   
    
    
    countercycles(AllCycles,Iperm,CounterCycles)




    # print("Permutation in counter-cycles:")
    # print("m =",end=" ")
    # for i in range (len(CounterCycles)):
    #     print("(",end=" ")
    #     for j in range(len(CounterCycles[i])):
    #         print(CounterCycles[i][j],end=" ")
    #     print(")",end=" ")

    # print()
    # if (numberswitcher(len(CounterCycles))==False):
    #     print("sgn(m)=-1 peritti")
    # else:
    #     print("sgn(m)=1 artia")







