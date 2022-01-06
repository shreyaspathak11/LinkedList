def count(lst):
    even=0
    odd=0
    for i in lst:
        if(i%2==0):
            even=even+1
        else:
            odd=odd+1
                

    return(even,odd)


lst = list(map(int,input("\nEnter the numbers : ").strip().split()))
even,odd=count(lst)
print("Even:{} and Odd:{}".format(even,odd)) 
      