import numpy as np
import matplotlib
import matplotlib.pyplot as plt


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

with open("points.txt","r") as file:
    #file=filter(None,file.read().split('\n'))
    file=file.read().split('\n')
    for i in range(len(file)):
        file[i]=file[i].split(" ")
        for j in range(len(file[i])):           
            file[i][j] = list(map(float,file[i][j][1:len(file[i][j])-1].split(',') ))
print(file)

print("equazion")
V=input()

V=V.split("=")[0].replace(" ","")

V=V.split("+")
print(V)

for i,k in enumerate(V):
    V[i] = k[:-1]
    if(V[i] == ""):
        V[i] = 1;
    elif(V[i] == "-"):
        V[i] = -1;
    else:
        V[i] =V[i]
print(V)
Vr = []
for item in V:
    Vr.append(float(item))

print(Vr)
del V

x1=[1,0,(-1)*Vr[0]/Vr[2]]
x2=[0,1,(-1)*Vr[1]/Vr[2]]
print(x1,x2)

#run GS on x1,x2
H=[np.array(x1),np.array(x2)]
Ver=GS(H)
for v in Ver:
    print(v)
#now take all points

Points=[]
for i in range(len(file)):
    if(file[i][0] not in Points):
        Points.append(file[i][0])
    

for i in range(len(file)):
    if(file[i][1] not in Points):
        Points.append(file[i][1])
        
print(Points)





finalPoints=[]
for i in range (len(Points)):
    
    finalPoints.append([np.inner(Points[i], Ver[0]),np.inner(Points[i], Ver[1])])


    print(finalPoints[i])

pointConnections=[]
j=0
for i in range (len(file)):
    pointConnections.append([])
    if(file[i][0]==Points[j]):
        pointConnections[j].append(Points.index(file[i][1]))
        print(j)
    else:
        j+=1
        pointConnections[j].append(Points.index(file[i][1]))
        print(j)

print(pointConnections)
##
##for i in range (len(finalPoints)):
##
##    plt.plot(finalPoints[i][0],finalPoints[i][1],'ro')
##
##    


for i in range(len(finalPoints)):
    if(len(pointConnections)==0):
        plt.plot(finalPoints[i][0],finalPoints[i][1],'ro-')
    else:
        for j in range(len(pointConnections[i])):
            plt.plot([finalPoints[i][0],finalPoints[pointConnections[i][j]][0]],[finalPoints[i][1],finalPoints[pointConnections[i][j]][1]],'ro-')

##
##x, y = np.random.random(size=(2,10))
##
##plt.plot([1,3], [1,3], 'ro-')
##
##plt.plot([1,2], [1,5], 'ro-')
plt.grid()

plt.show()

    
