
n=5
for i in range(n):
    for j in range(i+1):
        print("A",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i+1):
        print("U",end=" ")
    print()       

n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=1    
    print()  

n=5
p=66
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=1    
    print()    

n=5
p=65
for i in range(n):
    for j in range(i,n):
        print(chr(p),end=" ")
    p+=1    
    print()

n=5
p=69
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p-=1    
    print()   


n=5
p=69
for i in range(n):
    for j in range(i,n):
        print(chr(p),end=" ")
    p-=1    
    print()     

n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=2    
    print()    

n=5
p=65
for i in range(n):
    for j in range(i,n):
        print(chr(p),end=" ")
    p+=2    
    print()

n=5
for i in range(n):
    for j in range(i+1):
        if(i % 2 ==0):
            print("A",end=" ")
        else:
            print("B",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i,n):
        if(i % 2 ==0):
            print("A",end=" ")
        else:
            print("B",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i):
        print('',end=" ")
    for j in range(i,n):
        if(i % 2 ==0):
            print("z",end=" ")
        else:
            print("0",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i):
        print('',end=" ")
    for j in range(i+1):
        if(i % 2 ==0):
            print("z",end=" ")
        else:
            print("0",end=" ")
    print()

n=5
p=65
for i in range(n-1):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=1            
    print()








n=5
p=65
for i in range(n-1):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=1
    print()
for i in range(n):
    for j in range(i+1):
        print("",end=" ")
    for j in range(i,n-1):
        print(chr(p),end=" ")
    p-=1
    print()

n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1
    print()    

n=5
for i in range(n):
    p=65
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1
    print()

n=5
for i in range(n):
    p=65
    for j in range(i):
        print("",end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
        p+=1
    print()        

n=5
for i in range(n):
    p=65
    for j in range(i):
        print("*",end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
        p+=1
    print()

#Hill triangle

n=5
for i in range(n):
    p=65
    for j in range(i,n):
        print("",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p+=1
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1
    print()

n=5
for i in range(n):
    p=65
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i):
        print("o",end=" ")
        p+=1
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1
    print()

n=5
for i in range(n):
    p=69
    for i in range(i+1):
        print(chr(p),end=" ")
        p-=1
    print()

n=5
for i in range(n):
    p=69
    for i in range(i+1):
        print(chr(p),end=" ")
        p+=1
    print()

n=5
k=69
for i in range(n):
    p=k
    for j in range(i):
        print("",end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
        p-=1
    k-=1
    print()

n=5
k=69
for i in range(n):
    p=k
    for j in range(i):
        print("*",end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
        p-=1
    k-=1
    print()


n=5
for i in range(n):
    p=65
    for j in range(i,n):
        print("",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p+=1
    for j in range(i+1):
        print(chr(p),end=" ")
        p-=1        
    print()

n=5
for i in range(n):
    p=65
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p+=1
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1        
    print()


#CODER CHARATER PATTERN

s="CODER"
n=len(s)
p=0
for i in range(n):
    for j in range(i+1):
        print(s[p],end=" ")
    p+=1
    print()    

s="USMAN"
n=len(s)
p=0
for i in range(n):
    for j in range(i+1):
        print(s[p],end=" ")
    p+=1
    print()

s="CODER"
n=len(s)
p=0
for i in range(n):
    for j in range(i,n):
        print(s[p],end=" ")
    p+=1
    print()

s="CODER"
n=len(s)
p=0
for i in range(n):
    for j in range(i):
        print("",end=" ")
    for j in range(i,n):
        print(s[p],end=" ")
    p+=1
    print()

s="CODER"
n=len(s)
p=n-1
for i in range(n):
    for j in range(i+1):
        print(s[p],end=" ")
    p-=1
    print()    

s="USMAN"
n=len(s)
p=n-1
for i in range(n):
    for j in range(i+1):
        print(s[p],end=" ")
    p-=1
    print()


s="CODER"
n=len(s)
p=n-1
for i in range(n):
    for j in range(i):
        print("",end=" ")
    for j in range(i,n):
        print(s[p],end=" ")
    p-=1
    print()

s="CODER"
n=len(s)
for i in range(n):
    p=0
    for j in range(i+1):
        print(s[p],end=" ")
        p+=1
    print()

s="CODER"
n=len(s)
for i in range(n):
    p=n-1
    for j in range(i+1):
        print(s[p],end=" ")
        p-=1
    print()

s="CODER"
n=len(s)
for i in range(n):
    for j in range(i):
        print("",end=" ")
    p=n-1
    for j in range(i,n):
        print(s[p],end=" ")
        p-=1
    print()

s="CODER"
n=len(s)
k=n-1
for i in range(n):
    p=k
    for j in range(i):
        print("",end=" ")
    for j in range(i,n):
        print(s[p],end=" ")
        p-=1
    print()
    k-=1        




































































































































































