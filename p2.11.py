###A.M.:P19100
###Onoma:Aristotelis
###Epwnimo:Matakias
###Askisi E1 Efarmosmeni Algebra Ergasia I
###PYTHON 3.8 

"""
Arxika ftiaxnoume tis synartiseis 'gcd' kai 'ekp' gia na vriskoume tin
ta3i (order) mias metatheseis.

H synartisi 'g(x)' dexetai san orisma ton arithmo pou edwse o xristis
kai epistrefei tin megisti ta3i(order) gia tin opoia h metathesi einai
ginomeno 2 3enwn kyklwn.

Mesa stin 'g(x)' vrisketai h 'find_all_possible()' h opoia vriskei
ola ta pithana zeurargia mhkwn 3enwn kyklwn. Gia kathe zeugari vriskei to ekp
kai an einai megalytero tou 'max1' tote to 'max1' pairnei tin timi tou ekp.

"""


## Vriskoume to gcd me ton algorithmo tou Euklidi ##
## Isxuei : gcd(a, b) = gcd(b, u), opou u to ypoloipo ths diairesis tou a me to b ##
## Xrisimopoioume to mod - % ##
def gcd (a,b):   
    if b==0:
        return a
    return gcd(b, a % b)
## Me ton MKD eukola vriskoume to EKP ##
def ekp (a,b):
    return (a*b)/gcd (a,b)
 

def g(x):

    ##apantame amesws gia to 1 kai to 2 epeidi h 'find_all_possible'##
    ##leitourgei gia arithmous megalyterous tou 3##
   
    if x==1:
        print("Max order is 1")
        return
    if x==2:
        #print("[1, 1]")
        print("Max order is 1")
        return

    ## Ta zeuaria einai oi arithmoi 'a' kai 'b' kai exoun arxikes times ##
    ## To 'a' au3anetai kata 1 - To 'b' meiwnetai kata 1##
    a=1  
    b=x-1        
    max1=0
    ## Gia na min pairnoume ta idia zeuragia 2 fores stamatame otan ta a kai b einai isa h otan a>b ##

    def find_all_possible():

        nonlocal max1
            
        nonlocal a

        nonlocal b
        
        while True:

            if a==x or a>b:
                break   
            #print(a,b)                
            temp=int(ekp(a,b))

            if (temp > max1):
                max1=temp
            del temp
            if a==b :
                break

            a+=1
            b-=1

    find_all_possible()
    
    print ("Max order is",max1)
    return


## Elegxoume oti deinei o xristis me vroxo pou stamataei na zhtaei eisodo mexri na dwthei ##
## eggyrh eisodos (oxi charaktiras ,0 kai arnitikos arithmos) ##
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



