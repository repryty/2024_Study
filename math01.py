for i in range(5):
    i+=1
    i=i*60

    root_n=i**0.5
    a=int(str(root_n).split(".")[1])
    b=int(str(root_n/2).split(".")[1])
    c=int(str(root_n/3).split(".")[1])
    print(i**0.5)

    
    if root_n < root_n/2 and root_n/2 < root_n/3:
        print(i)
