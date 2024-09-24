
n=5
for i in range(n):
    for j in range(i+1):
        print("A",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i+1):
        print("B",end=" ")
    print()    

n=5
for i in range(n):
    for j in range(i,n):
        print("C",end=" ")
    print()    

n=5
for i in range(n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")    
    print()

n=5
for i in range(n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("A",end=" ")    
    print()    

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("A",end=" ")
    for j in range(i+1):
        print("A",end=" ")        
    print()

n=5
for i in range(n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("A",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("A",end=" ")            
    print()    

n=5
for i in range(n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("A",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("B",end=" ")            
    print()

n=5
for i in range(n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")                    
    print()    

n=5
for i in range(n+1):
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")                    
    print()    

n=5
for i in range(n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ") 
    print()
for i in range(n):
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")                    
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
    for j in range(i,n):
        print(chr(p),end=" ")
    p+=1    
    print()

n=5
p=69
for i in range(n):
    for j in range(i,n):
        print(chr(p),end=" ")
    p-=1    
    print()

n=5
p=69
for i in range(n):
    for j in range(i+1):
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

n=6
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=2    
    print()   

n=5
p=74
for i in range(n):
    for j in range(i,n):
        print(chr(p),end=" ")
    p-=2    
    print()

n=5
p=75
for i in range(n):
    for j in range(i,n):
        print(chr(p),end=" ")
    p-=2    
    print()

n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=3    
    print()

n=6
p=65
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")    
    p+=1  
    print()

n=5
p=63
for i in range(n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
    p+=2        
    print()

n=5
p=66
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
    p+=1
    for j in range(i+1):
        print(chr(p),end=" ")
    p-=1            
    print()

n=5
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print("A",end=" ")
        else:
            print("B",end=" ")    
    print()

n=5
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print("B",end=" ")
        else:
            print("C",end=" ")    
    print()    

n=6
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print("B",end=" ")
        else:
            print("A",end=" ")    
    print()

n=5
for i in range(n):
    for j in range(i,n):
        if(i%2==0):
            print("A",end=" ")
        else:
            print("B",end=" ")    
    print()

n=5
for i in range(n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        if(i%2==0):
            print("B",end=" ")
        else:
            print("A",end=" ")        
    print()

n=5
for i in range(n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        if(i%2==0):
            print("A",end=" ")
        else:
            print("B",end=" ")        
    print()

n=5
for i in range(n):
    for j in range(i,n):
        if(i%2==0):
            print("1",end=" ")
        else:
            print("2",end=" ")
    for j in range(i):
        if(i%2==0):
            print("3",end=" ")
        else:
            print("4",end=" ")
    for j in range(i+1):
        if(i%2==0):
            print("5",end=" ")
        else:
            print("6",end=" ")  
    for j in range(i,n):
        if(i%2==0):
            print("7",end=" ")
        else:
            print("8",end=" ")                                      
    print()

n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        if(i%2==0):
            print("z",end=" ")
        else:
            print("0",end=" ")        
    print()


#character diamond pattern

n=5
p=65
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=1            
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(chr(p),end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
    p+=1            
    print()    

n=5
p=65
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=1            
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(chr(p),end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
    p-=1            
    print()    

n=5
p=65
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=1            
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(chr(p),end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
    p+=2            
    print()  

n=5
p=65
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=1            
    print()
q=97
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(chr(q),end=" ")
    for j in range(i,n):
        print(chr(q),end=" ")
    q+=1            
    print()    


n=5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        if(i%2==0):
            print("A",end=" ")
        else:
            print("B",end=" ")
    for j in range(i+1):
        if(i%2==0):
            print("A",end=" ")
        else:
            print("B",end=" ")                   
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        if(i%2==0):
            print("A",end=" ")
        else:
            print("B",end=" ")
    for j in range(i,n):
        if(i%2==0):
            print("A",end=" ")
        else:
            print("B",end=" ")                    
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
    p=66
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1
    print()


#Left triangle
n=5
for i in range(n):
    p=65
    for j in range(i,n):
        print(chr(p),end=" ")
        p+=1
    print()

n=5
for i in range(n):
    p=69
    for j in range(i,n):
        print(chr(p),end=" ")
        p-=1
    print()

n=5
for i in range(n+1):
    for j in range(i,n):
        print(" ",end=" ")
    p=65    
    for j in range(i):
        print(chr(p),end=" ")
        p+=1  
    print()     

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    p=65
    for j in range(i):
        print(chr(p),end=" ")
        p+=1
    p=65    
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1       
    print()

n=5
for i in range(n):
    p=65
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p+=1
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1        
    print()

n=5
for i in range(n-1):
    p=65
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p+=1
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1        
    print()
for i in range(n):
    p=65
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(chr(p),end=" ")
        p+=1
    for j in range(i,n):
        print(chr(p),end=" ")
        p+=1        
    print()    

n=5
for i in range(n):
    p=65
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
        p+=2    
    print()

n=5
for i in range(n):
    p=69
    for j in range(i+1):
        print(chr(p),end=" ")
        p-=1
    print()

n=6
for i in range(n):
    p=70
    for j in range(i+1):
        print(chr(p),end=" ")
        p-=1
    print() 

n=5
for i in range(n):
    p=69
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
        p-=1    
    print()

n=5
for i in range(n):
    p=69
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
        p-=1    
    print()

n=5
for i in range(n+1):
    p=69
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p+=1    
    print()   

n=5
for i in range(n):
    p=74
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p-=1
    for j in range(i+1):
        print(chr(p),end=" ")
        p-=1        
    print()

n=5
for i in range(n):
    p=65
    for j in range(i,n):
        print(" ",end=" ")
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
        print(" ",end=" ")
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
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(chr(p),end=" ")
        p+=1
    for j in range(i,n):
        print(chr(p),end=" ")
        p-=1     
    print() 

s="CODER"
n=len(s)
p=0
for i in range(n):
    for j in range(i+1):
        print(s[p],end=" ")
    p+=1    
    print()

s="PYTHON"
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
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(s[p],end=" ")
    p+=1        
    print()

s="CODER"
n=len(s)
p=0
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(s[p],end=" ")
    for j in range(i+1):
        print(s[p],end=" ")
    p+=1            
    print()

s="PROGRAM"
n=len(s)
p=0
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(s[p],end=" ")
    for j in range(i,n):
        print(s[p],end=" ")
    p+=1            
    print()

s="CODER"
n=len(s)
p=0
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(s[p],end=" ")
    for j in range(i+1):
        print(s[p],end=" ")
    p+=1            
    print()
s="CODER"
n=len(s)
p=0
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(s[p],end=" ")
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

s="CODER"
n=len(s)
p=n-1
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(s[p],end=" ")
    p-=1        
    print()

s="CODER"
n=len(s)
p=n-1
for i in range(n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(s[p],end=" ")
    p-=1        
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
for i in range(n+1):
    p=n-1
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(s[p],end=" ")
        p-=1    
    print()

s="CODER"
n=len(s)
for i in range(n):
    p=n-1
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(s[p],end=" ")
        p-=1    
    print()    

s="CODER"
n=len(s)
k=n-1
for i in range(n):
    p=k
    for j in range(i+1):
        print(s[p],end=" ")
        p-=1
    print()
    k-=1

s="CODER"
n=len(s)
k=n-1
for i in range(n):
    p=k
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(s[p],end=" ")
        p-=1    
    print()
    k-=1

s="CODER"
n=len(s)
k=n-1
for i in range(n+1):
    p=k
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(s[p],end=" ")
        p-=1    
    print()
    k-=1 


































    










































































































































































