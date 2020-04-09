
def gcd (a,b):

    if b==0:
        return a
    return gcd(b, a % b)

def ekp (a,b):

    return (a*b)/gcd (a,b)


def g(x):

    s=2

    ls=[]


    burned=[]

    start=1


    while (start<x-2 and start not in burned):

        element=[]

        element.append(start)

        element.append(0)

        def lol():

            for i in range(1,x):

                if (element[0]+i==x):
                    
                    element[1]=(i)
                    burned.append(i)
                    
            print (element)

            if (element[0]!=element[1]):
                ls.append(ekp(element[0],element[1]))
        

        lol()
        start+=1

    print (max(ls))


g(6)
