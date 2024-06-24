
#Square pattern

print("*")

n=5
for i in range(n):
    print("*")

n=5
for i in range(n):
    print("*",end="")

n=5
for i in range(n):
    print("*",end=" ")   

n=5
for i in range(n):
    for j in range(n):
        print("*")    

n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")    

n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

n=6
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()  

n=6
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

n=5
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1):
            print("*",end=" ")
    print()    

n=5
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1):
            print("*",end=" ")

n=5
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        

n=5
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1):
            print("*",end=" ")
        else:
            print("",end=" ")    
    print()

n=5
for i in range(n):
    for j in range(n):
        if(i==n//2 or j==n//2):
            print("*",end=" ")
        else:
            print("",end=" ")    
    print()

#Cross pattern

n=5
for i in range(n):
    for j in range(n):
        if(i==j or i+j==n-1):
            print("*",end=" ")
        else:
            print("",end=" ")    
    print()

#Hollow square pattern

n=5
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=" ")
        else:
            print("",end=" ")    
    print()

#Hollow increasing triangle

n=5
for i in range(n):
    for j in range(i+1):
        if(i==n-1 or j==0 or j==i):
            print("*",end=" ")
        else:
            print("*",end=" ")
    print()       

n=5
for i in range(n):
    for j in range(i+1):
        if(i==n-1 or j==0 or j==i):
            print("*",end=" ")
        else:
            print("",end=" ")    
    print()

#Hollow Decreasing Triangle

n=5
for i in range(n):
    for j in range(i,n):
        if(i==0 or j==1 or j==n-1):
            print("*",end=" ")
        else:
            print("*",end=" ")    
    print()

n=5
for i in range(n):
    for j in range(i,n):
        if(i==0 or j==1 or j==n-1):
            print("*",end=" ")
        else:
            print("",end=" ")    
    print()

#Hollow hill pattern

n=5
for i in range(n):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i):
        if(i==n-1 or j==0):
            print("*",end=" ")
        else:
            print("",end=" ")
    for j in range(i+1):
        if(i==n-1 or j==i):
            print("*",end=" ")
        else:
            print("",end=" ")                    
    print()

#Hollow Diamond pattern

n=5
for i in range(n-1):
    for j in range(i,n-1):
        print("",end=" ")
    for j in range(i):
        if(j==0):
            print("*",end=" ")
        else:
            print("",end=" ")
        for j in range(i+1):
            if(j==i):
                print("*",end=" ")
            else:
                print("",end=" ")
for i in range(n):
    for j in range(i):
        print("",end=" ")
    for j in range(i,n):
        if(j==i):
            print("*",end=" ")
        else:
            print("",end=" ")
    for j in range(i,n-1):
        if(j==n-2):
            print("*",end=" ")
        else:
            print("",end=" ")                                                    
    print()






























































