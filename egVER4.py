import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#Aristotelis Matakias P19100
#Efarmosmeni Algebra 3.2

#
##
####
######
########
##########
############
###################- Gram - Schmidt (functions) -########################
def inner(u,v):
    return np.vdot(u,v)

def GS_product(y):
    return 1/np.sqrt(inner(y,y))*y

def GS(W):
    W2=[GS_product(W[0])]
    for i in range(1,len(W)):
        s=W[i]
        for j in range(i):
            s=s-inner(W[i],W2[j])*W2[j]
        W2.append(GS_product(s))
    return W2
###################################### > -   MAIN  -  < ########################

print("Give numbers a,b,c of ax + by + cz = 0")

print("a is:")
a = input()
print("b is:")
b = input()
print("c is:")
c = input()

W=[]

W.append(float(a))
W.append(float(b))
W.append(float(c))
del a,b,c

#now create x1,x2 vectors
x1=[]
x2=[]

#if none is zero
if(W[0]!=0 and W[1]!=0 and W[2]!=0):
    x1=[1,0,(-1)*W[0]/W[2]]
    x2=[0,1,(-1)*W[1]/W[2]]

#if one is zero
elif(W[0]==0 and W[1]!=0 and W[2]!=0):
    x1=[1,0,0]
    x2=[0,(-1)*W[2]/W[1],1]
elif(W[0]!=0 and W[1]==0 and W[2]!=0):
    x1=[0,1,0]
    x2=[(-1)*W[2]/W[0],0,1]
elif(W[0]!=0 and W[1]!=0 and W[2]==0):
    x1=[0,0,1]
    x2=[(-1)*W[1]/W[0],1,0]
    
#if 2 are zero
elif(W[0]==0 and W[1]==0 and W[2]!=0):    
    x1=[1,0,0]
    x2=[0,1,0]
elif(W[0]==0 and W[1]!=0 and W[2]==0):    
    x1=[1,0,0]
    x2=[0,0,1]
elif(W[0]!=0 and W[1]==0 and W[2]==0):    
    x1=[0,0,1]
    x2=[0,1,0]
    
#if all are zero    
elif(W[0]==0 and W[1]==0 and W[2]==0): 
    x1=[1,0,0]
    x2=[0,1,0]


#run GS on x1,x2
Ver=[]    
H=[np.array(x1),np.array(x2)]
Ver=GS(H)
#for v in Ver:
    #print(v)
    

#read the file
print("Give the name of the file")
name=input()
    
with open(name,"r") as file:
    #file=filter(None,file.read().split('\n'))
    file=file.read().split('\n')
    for i in range(len(file)):
        file[i]=file[i].split(" ")
        for j in range(len(file[i])):           
            file[i][j] = list(map(float,file[i][j][1:len(file[i][j])-1].split(',') ))
#print(file)

    
#now take all points

Points=[]
for i in range(len(file)):
    if(file[i][0] not in Points):
        Points.append(file[i][0])
    

for i in range(len(file)):
    if(file[i][1] not in Points):
        Points.append(file[i][1])
        
#print(Points)

#find the connections

pointConnections=[]
j=0
for i in range (len(file)):
    pointConnections.append([])
    if(file[i][0]==Points[j]):
        pointConnections[j].append(Points.index(file[i][1]))
        #print(j)
    else:
        j+=1
        pointConnections[j].append(Points.index(file[i][1]))
        #print(j)

#print(pointConnections)
   

#now find the final points and draw them


def product_points(Points,finalPoints,pointConnections,Ver):
    finalPoints=[]
    for i in range (len(Points)):
        
        finalPoints.append([np.inner(Points[i], Ver[0]),np.inner(Points[i], Ver[1])])
        #print(finalPoints[i])


    for i in range(len(finalPoints)):
        if(len(pointConnections)==0):
            plt.plot(finalPoints[i][0],finalPoints[i][1],'ro-')
        else:
            for j in range(len(pointConnections[i])):
                plt.plot([finalPoints[i][0],finalPoints[pointConnections[i][j]][0]],[finalPoints[i][1],finalPoints[pointConnections[i][j]][1]],'ro-')

    return finalPoints

finalPoints=[]
finalPoints=product_points(Points,finalPoints,pointConnections,Ver)

plt.grid()

plt.show()

    
