
def gcd (a,b):

    if b==0:
        return a
    return gcd(b, a % b)

def ekp (a,b):

    return (a*b)/gcd (a,b)


def g(x):


    if x==1:
        print("Cannot be expressed with counter cycles!")
        return
    if x==2:
        print("[1, 1]")
        print("1")
        return

    ls=[]

    burned=[]

    start=1

    while (start<x-1 and start not in burned):

        element=[]

        element.append(start)

        element.append(0)

        def find_all_possible():

            for i in range(1,x):

                if (element[0]+i==x):
                    
                    element[1]=(i)
                    burned.append(i)
                    
            print (element)

            if (element[0]!=element[1]):
                ls.append(ekp(element[0],element[1]))
        

        find_all_possible()
        start+=1

    print (int(max(ls)))




while True:
    try:
        a = int(input("Please enter a possitive number: "))
        if a<=0:
            print("Oops!  That was no valid number.  Try again...")
            continue
        g(a)
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")



