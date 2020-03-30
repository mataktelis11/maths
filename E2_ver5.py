import numpy as np

###A.M.:P19100
###Onoma:Aristotelis
###Epwnimo:Matakias
###Askisi E2 Diakrita Mathimatika Ergasia I
###PYTHON 3.8
# 
## using numpy
 


"""
Synartisi 'hypercube' :

Pairnei san eisodo to n kai epistrefei tin mitra geitniasis gia ton yperkivo Qn
se morfi array tis numpy

H synartisi kataskeuazei to Qn me auton ton anadromiko typo:

        | Qn-1    In-1 |                    
Qn =    |              |  , gia n>1 , opou Q1 = |0   1|
        | In-1    Qn-1 |                        |1   0|
"""



def hypercube(n):
    
    if n == 0:
        return np.array([[0]])
    else:
        Q = hypercube(n-1)
        I = np.eye(len(Q), dtype=int)
        return np.block([
            [Q, I],
            [I, Q],
        ])


"""
Gia na vroume enan kyklo Hamilton tha xrisimopoihsoume tin methodo 'Backtracking'

Arxika exoume mia lista , tin x , me mikos iso me ton arithmo twn korifwn tou grafimatos 
Ta stoixeia tis listas exoun arxika timi 0
Sto prwto stoixeio tis listas dinoume tin timi 1. Den paizei rolo poia 
timi tha dwsoume epeidi den allazei o kyklos

Arxizoume kai dinoume times sta stoixeia tis listas 3ekinwntas 
apo to deutero(afou to prwto exei hdh symplirwthei).
Oi times autes antistoixoun stis korifes tou grafimatos

Otan dinoume mia timi se ena stoixeio prepei na elegxoume:

-an syndeetai to me to proigoumeno stoixeio
-an to stoixeio hdh yparxei stin lista
-an to stoixeio einai to teleutaio stoixeio tis listas na syndeetai me to 1 (to prwto)

H synartisi 'theNextValueOfX(k)' dinei sto stoixeio tis theshs 'k' tis listas x 
oles tis times apo to 1 mexri tin teleutaia korifi kai stamataei an eikanopoiountai oles oi proipotheseis
An kanena stoixeio den  einai egyro tote  h synartisi tha dwsei tin timi 0

------

O kyklos Hamilton tha vrethei me tin synartisi 'hamilton(v)'
h synartisi auti kalei tin theNextValueOfX gia to stoixeio v tis listas.
An anoixneusei 0 stamataei
An den vrisketai sto telos tis listas kalei to hamilton(v+1)
H synartisi auti mporei na vrei olous tous dynatous kyklous Hamilton kai
tin periorizoume na stamataei stin prwti apantisi
An den yparxei apantisi den yparxei Kyklos Hamilton

"""

def theNextValueOfX(k):
                
    while True:
                    
        x[k]=(x[k]+1)%(len(graph)+1)
                    
        if  x[k]==0:
            return 
                    
        if ((graph[x[k-1]-1][x[k]-1]==1)==True):
                        
            for j in range(len(x)):
                            
                if x[j]==x[k]:
                              
                    break  
                        
                        
            if(j==k):
                
                if(k<len(x))or((k==(len(x)-1))and(graph[x[0]-1][x[k]-1]==1)):
                    if ((k==(len(x)-1))and(graph[x[0]-1][x[k]-1]==1)):
                        dummy=x.copy()
                        answers.append(dummy)   
                            
                    return
                        

def hamilton(v):
    
    while True:
        theNextValueOfX(v)
        if(x[v]==0):
            return
        if (v==len(x)-1):
            
            break
                    
        else:
            if len(answers)!=1:            
                hamilton(v+1)
            else:
                break           
                       
            
            



while True:
    try:
        a = int(input("Please enter a non negative integer: "))

        if(a==0):
            x1=hypercube(a)
           
            graph=x1.tolist()
           
            del x1


            print("Qn is:")
            for z in graph:
                print(z)
            
            del z
            
            print("There is no Hamilton Cycle")

            break

        if(a>0):


            
            x1=hypercube(a)
           
            graph=x1.tolist()
           
            del x1


            print("Qn is:")
            for z in graph:
                print(z)
            
            del z
            del a
            
            global x
            x=[]
            for y in range(len(graph)):
                x.append(0)
            x[0] = 1
            
            
            
            answers=[]
            dummy=[]
            hamilton(1)
            
            if(len(answers))!=0:
                print("Hamilton Cycle is")
                answers[0].append(1)
                print(answers[0])
            else:
                print("There is no Hamilton Cycle")
            break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")








