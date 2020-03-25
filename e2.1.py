import numpy as np
            

def hypercube(ndim, diagonal=False):
    """Recursively construct the edge-connectivity of a hypercube

    Parameters
    ----------
    ndim : int
        Dimension of the hypercube
    diagonal : bool
        Value of the diagonal
        If True, vertices are considered connected to themselves

    Returns
    -------
    ndarray, [2**ndim, 2**ndim], bool
        connectivity pattern of the hypercube
    """
    if ndim == 0:
        return np.array([[diagonal]])
    else:
        D = hypercube(ndim-1, diagonal)
        I = np.eye(len(D), dtype=D.dtype)
        return np.block([
            [D, I],
            [I, D],
        ])




def  connection(k,l):

    ##prints true if k and l are connected in the graph
    
    if (graph[k][l]==1):
        return True
        


    return False
    



def displayCycle():
    print("cycle is ")
    for i in range(len(graph)):
        print(path[i])
    print(path[0])


def isValid(v,k):
    if (graph[path[k-1]][v]==0):
        return False
    for i in range(k):
        if (path[i]==v):
            return False
    return True

def cycleFound(k):
    if(k==len(graph)):
        if (graph[path[k-1]][path[0]] == 1 ):
            return True
        else:
            return False
    for v in range(1,len(graph)):
        if(isValid(v,k)):
            path[k] = v
            if (cycleFound(k+1) == True):
                return True
            path[k]=-1
    return False





while True:
    try:
        a = int(input("Please enter a non negative integer: "))
        if(a>=0):


            print("Qn is:")
            x1=hypercube(a)

            x2=[]
            x22=[]
            for g in x1:
                for j in g:
                    if j==True:
                        x22.append(1)
                    else:
                        x22.append(0)

                x2.append(x22)
                x22=[]
            for w in x2:
                print(w)

            graph=x2
            path=[]
            for y in range(len(graph)):
                path.append(0)
            for i in range(len(graph)):
                path[i] = -1
            path[0] = 0

            if ( cycleFound(1) == False ) :
                print("no")
            else:
                for z in range(len(path)):
                    path[z]+=1
                displayCycle()


            break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")








