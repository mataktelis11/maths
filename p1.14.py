###A.M.:P19100
###Onoma:Aristotelis
###Epwnimo:Matakias
###Askisi E1 Efarmosmeni Algebra Ergasia I
###PYTHON 3.8 

"""
Arxika pername ta moumera pou mas edwse o xristis se ena lexiko
to opoio exoume arxikopoihsei ws 'permutation'

Otan o xristis deinei ta noumera mporei na afisei osa kena thelei.
An omws yparxoun mh eggyroi xaraktires ( xaraktires pou den einai akaireai ) to programma 
den tous dexetai kai afinei ton xristi na 3anadokimasei

Stin synexeia ginetai elegxos an einai pragmati metathesi me tin synartisi 'checkpermutation'
h opoia elegxei an yparxoun epanali3eis h mh-thetikoi arithmoi kai epistrefei 'True' h 'False'

Efwson h 'checkpermutation' epistre3ei 'True' to programma synexizei
me tin synartisi 'printpermutation' h opoia dexetai san orisma to le3iko 'permutation' kai
mia metavliti boolean tin 'Iperm' pou exoume arxikopoihsei ws 'True'

H synartisi 'checkpermutation' ektipwnei tin metathesh kai to mikos ths kai elgexei
ab h metathesh einai tautotikh kai stin periptwsh pou auto isxuei h 'Iperm' tha einai 'True'
alliws 'False'

Akolouthei h  synatrisi'oppositeofpermutation' dexetai san orisma to le3iko 'permutation'
kai ektipwnei tin antistrofh tis metathshs.

Meta h synartisi 'findcycles' (dexetai san orisma to le3iko 'permutation') 
topothetei sto keno array 'AllCycles' olous tous kyklous ths metatheshs

H synartisi 'printallcycles' ektipwnei tin metathesei san ginomeno 
olwn twn kwklwn

H synartisi 'printstrangecycles' ektipwnei tin metathesei san ginomeno 
3enwn kyklwn (den ektypwnei tous kyklous me mhkos 1) 

An h metathesi einai tautotiki h exei mono ena stoixeio ( m=(1) )
tote kaleitai mono h synartisi 'printallcycles' alliws,
kalountai kai oi 'printallcycles' kai 'printstrangecycles'.

Telos kaleitai h synartisi 'countercycles':

    Arxika elegxei an h metathesh exei toulaxiston 2 stoixeia (alliws aktypwnei oti den mporei h
    metathesh na ekfrastei san ginomeno antimetathesewn)

    H synartisi auti dexetai san orisma to array 'AllCycles' , tin boolean 'Iperm' kai to
    keno array 'CounterCycles'

    H synartisi gemiszei to array 'CounterCycles' me tis antimetathesei ths metatheshs

    An omws h metathesh einai tautotikh tote grafetai san ginomeno twn antimetathesewn:
    (1,2)(1,2).

    To sgn elegxeitai apo to mhkos tou array 'CounterCycles' me tin synartisi 'numberswitcher'

"""



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


## elegxei an o arithmos n einai artios h perritos allazontas n fores mia boolean metavliti
## An exei idia timi me tin arxikh tha einai zigos alliws perritos
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
        print("H metathesi einai tautotiki")
    print("Lenght of permutation is:",len(permutation))

    return Iperm

def oppositeofpermutation(permutation):

    print("Antistrofi tis metathesis:")
    print("m^(-1) =(",end=" ")

    
    for i in range(1,len(permutation)+1):
        for j in range(1,len(permutation)+1):
            if(permutation[j]==i):
                print(j,end=" ")       
    print(")")


def countercycles(AllCycles,Iperm,CounterCycles):
    if(len(permutation)<2):
        print("Den mporei na ekfrastei san ginomeno antimetathesewn")
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


        print("Metathesi san ginomeno antimetathesewn:")
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

    print("Metathesi san ginomeno kyklwn:")
    print("m =",end=" ")
    
    for i in range (len(AllCycles)):
        
        print("(",end=" ")
        for j in range(len(AllCycles[i])):
            print(AllCycles[i][j],end=" ")
        print(")",end=" ")

    print()

def printstrangecycles():

    print("Metathesi san ginomeno 3enwn kyklwn:")
    print("m =",end=" ")
    
    for i in range (len(AllCycles)):
        if(len(AllCycles[i])==1):
            continue
        print("(",end=" ")
        for j in range(len(AllCycles[i])):
            print(AllCycles[i][j],end=" ")
        print(")",end=" ")

    print()

################################### M A I N () #######################################

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



