###A.M.:P19100
###Onoma:Aristotelis
###Epwnimo:Matakias
###Askisi E1 Efarmosmeni Algebra Ergasia I
###PYTHON 3.8 

"""
Arxika ftiaxnoume tis synartiseis 'gcd' kai 'ekp' gia na vriskoume tin
ta3i (order) mias metatheseis

Stin synexeia me tin synartisi g ftiaxnoume ola ta pythana
di-synola twn opoion ta stoixeia exoun athroisma iso me ton arithmo pou mas
edwse o xristis

Ousiastika einai ola ta pithana zeuragia mikwn twn 3enwn kyklwn apo
tous opoious mporei na apoteleitai mia metathesi tou 'n'

Gia kathe mia periptwsi vriskoume to ekp kai to vazoume se mia lista
Apantisi tha einai to megisto stoixeio autis tis listas

"""



def gcd (a,b):

    if b==0:
        return a
    return gcd(b, a % b)

def ekp (a,b):

    return (a*b)/gcd (a,b)
 




def g(x):

    max1=0
   

    if x==1:
        print("Cannot be expressed with counter cycles!")
        return
    if x==2:
        print("[1, 1]")
        print("1")
        return

    a=1
  
    b=x-1

    

        

    def find_all_possible():

        nonlocal max1
            
        nonlocal a

        nonlocal b
        
        while True:

            if a==x:
                break   
            #print(a,b)
            
                
            temp=int(ekp(a,b))

            if (temp > max1):
                max1=temp

            a+=1
            b-=1

    find_all_possible()
        

    #print (int(max(ls)))
    print (max1)



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



