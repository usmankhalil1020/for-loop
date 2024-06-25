
#Arthmetic series

sum = 0
n=int(input("enter n"))
for i in range(1,n+1):
    sum=sum+i
print("sum of series =",sum)    

sum = 0
a = 1
n=int(input("enter n"))
for i in range(1,n+1):
    sum=sum+a
    a+=1
print("Sum of series =",sum)    

# 9+13+17...N

sum=0
a=9
n=int(input("enter n"))
for i in range(1,n+1):
    sum=sum+a
    a+=4
print("Sum of series =",sum)    

#2+4+6+8...N

sum=0
a=2
n=int(input("enter n"))
for i in range(1,n+1):
    sum=sum+a
    a+=2
print("sum of series =",sum)

#1+3+5+7...N

sum=0
a=1
n=int(input("enter n"))
for i in range(1,n+1):
    sum=sum+a
    a+=2
print("sum of series =",sum)

#10+9+8...N

sum=0
a=10
n=int(input("enter n"))
for i in range(1,n+1):
    sum=sum+a
    a-=1
print("sum of series =",sum)

#x^1 + x^2 + x^3 + x^4...N

sum=0
a=1
n=int(input("enter n"))
x=int(input("enter X"))
for i in range(1,n+1):
    sum=sum + x**a
    a+=1
print("sum of series =",sum)

#9!/x + 13!/x + 17!/x...N

import math as m
sum=0
a=9
n=int(input("enter n"))
x=int(input("enter X"))
for i in range(1,n+1):
    sum=sum + m.factorial(a)/x
    a+=4
print("sum of series =",sum)

#2^x + 4^x + 6^x +8^x...20

sum=0
a=2
x=int(input("enter x"))
for i in range(1,n+1):
    sum=sum+a**x
    a+=2
print("sum of series =",sum)

#1^3/x + 3^3/x + 5^3/x + 7^3/x...N

sum=0
a=1
n=int(input("enter n"))
x=int(input("enter X"))
for i in range(1,n+1):
    sum=sum + a**3/x
    a+=2
print("sum of series =",sum)

#2/10 + 4/9 + 6/8 + 8/7...20/1

sum = 0
a=2; d=10
N=10
x=int(input("enter x"))
for i in range(1,n+1):
    sum=sum + a/d
    a+=2; d-=1
print("sum of series =",sum)

#Geometric Series

#2 + 4 + 8 + 16...N

sum=0
k=2   #product
n=int(input("enter n"))
for i in range(1,n+1):
    sum=sum + k
    k=k*2
print("sum of series =",sum)   

#2 + 6 + 18 + 54...N

sum=0
k=2   
n=int(input("enter n"))
for i in range(1,n+1):
    sum=sum + k
    k=k*3
print("sum of series =",sum)

#10 + 30 + 90 + 270...N

sum=0
k=10 
n=int(input("enter n"))
for i in range(1,n+1):
    sum=sum + k
    k=k*3
print("sum of series =",sum)

#5 + 25 + 125...N

sum=0
k=5
n=int(input("enter n"))
for i in range(1,n+1):
    sum=sum + k
    k=k*5
print("sum of series =",sum)

#x/2 + x/4 + x/8 + x/16...N

sum=0
x=int(input("enter x"))
n=int(input("enter n"))
k=2
for i in range(1,n+1):
    sum=sum + x/k
    k=k*2
print("sum of series =",sum)

#2-6+18-54...N

sum=0
x=int(input("enter x"))
n=int(input("enter n"))
k=2
for i in range(1,n+1):
    if i % 2 ==0:
        sum=sum-k
    else:
        sum=sum+k    
    sum=sum + k
    k=k*3
print("sum of series =",sum)

#x+2/10 + x+4/30 + x+6/90+...N

sum=0
x=int(input("enter x"))
n=int(input("enter n"))
a=2; k=10
for i in range(1,n+1):
    sum=sum + (x + a)/k
    a=a + 2; k = k * 3
print("sum of series =",sum)

#x+5^2/1+2 + x+25^2/2+3 +...N

import math as m
sum=0
x=int(input("enter x"))
n=int(input("enter n"))
k=5; a1=1; a2=2
for i in range(1,n+1):
    sum+=(x*k**2)/(a1+m.factorial(a2))
    k*=5; a1+=1; a2+=1
print("sum of series =",sum)
















































































