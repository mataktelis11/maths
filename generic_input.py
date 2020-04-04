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
                    
                permutation[index]=i
                index += 1
            else:
                print("TYPED invalid:Only possitive integers")
                check=False
                break
        if(check!=False):        
            break
    except ValueError:
        print("TYPED invalid:Only numbers and spaces")
        


del index
