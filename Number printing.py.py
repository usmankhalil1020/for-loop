
#Number program

#Print all digits of a number on different lines

n=268
m=n
while m!=0:
    d = m % 10
    print(d)
    m=m//10

n=373
m=n
while m!=0:
    d = m % 10
    print(d)
    m=m//10

n=100
m=n
while m!=0:
    d = m % 10
    print(d)
    m=m//10

n=2468
m=n
while m!=0:
    d = m % 10
    print(d)
    m=m//10

#Check if a number is palindrome or not eg 121

n=268
m=n
sum=0
while m!=0:
    d=m%10
    sum = sum * 10 + d
    m=m//10
if sum==n:
    print("yes")
else:
    print("no")


n=121
m=n
sum=0
while m!=0:
    d = m % 10
    sum = sum * 10 + d
    m = m//10
if sum==n:
    print("yes")
else:
    print("No")

#Check if a number is spy number or not. Means sum its digits equals the product of the digits. eg 123.1+2+3=1*2*3    

n=123
m=n
sum=0; prod=1
while m!=0:
    d=m % 10
    sum = sum + d; prod = prod * d
    m = m // 10
if sum==prod:
    print("Yes")
else:
    print("No")    

#Check if a number is special number or not . Sum of digits plus product of digits it is equal to orignal number eg 59=5+9+5*9     

n=59
m=n
sum = 0; prod = 1
while m!=0:
    d = m % 10
    sum = sum + d; prod = prod * d
    m = m // 10
if (sum + prod) == n:
    print("Yes")
else:
    print("No")    


#Check if a number is Harshad/Niven number or not . A number which is divisible by the sum of its digit. eg 156=1+5+6=12

n=156
m=n
sum = 0
while m!=0:
    d=m % 10
    sum = sum + d
    m = m // 10
if m % sum == 0:
    print("Yes")
else:
    print("No")        


n=169
m=n
sum = 0
while m!=0:
    d=m % 10
    sum = sum + d
    m = m // 10
if m % sum == 0:
    print("Yes")
else:
    print("No")

#Check if a number is duck number or not . A number which has zeros present in it eg: 402,280


n=402
m=n
count = 0
while m!=0:
    d = m % 10
    if d==0: count +=1
    m=m // 10
if count > 0:
    print("Yes")
else:
    print("No")        

n=398
m=n
count = 0
while m!=0:
    d = m % 10
    if d==0: count +=1
    m=m // 10
if count > 0:
    print("Yes")
else:
    print("No")

#Check if a number is Neon number or not. Where sum of digits of square of a number is equal to the number eg 9,9*9=81, 9=8 + 1

n=81
m=n
sum = 0; m = n * n
while m!=0:
    d = m % 10
    sum = sum + d
    m = m // 10
if sum==n:
    print("Yes")
else:
    print("No")        

n=78
m=n
sum = 0; m = n * n
while m!=0:
    d = m % 10
    sum = sum + d
    m = m // 10
if sum==n:
    print("Yes")
else:
    print("No")

#Check if a number is Automorphic number or not. It is a number which is contained in the last digit(s) of its square eg 25 in 625

n=625
m=n
flag = 0; q = n * n
while m!=0:
    d = m % 10; d1 = q % 10
    if d!=d1 : flag = 1  
    m = m // 10; q = q // 10
if flag == 0:
    print("Yes")
else:
    print("No")        

n=621
m=n
flag = 0; q = n * n
while m!=0:
    d = m % 10; d1 = q % 10
    if d!=d1 : flag = 1  
    m = m // 10; q = q // 10
if flag == 0:
    print("Yes")
else:
    print("No") 

#Check if a number is KM, special number or not. Where sum of factorial of digits is equal to the number eg 145=1! + 4! + 5!

import math
n=145
m=n
sum = 0
while m!=0:
    d = m % 10
    sum = sum + math.factorial(d)
    m = m // 10
if sum==n:
    print("Yes")
else:
    print("No")        

import math
n=136
m=n
sum = 0
while m!=0:
    d = m % 10
    sum = sum + math.factorial(d)
    m = m // 10
if sum==n:
    print("Yes")
else:
    print("No")

#Factor program

#Find if a number is a prime number. Prime number is a number divisible by 1 and itself. eg 5 has factor 1,5

n=5
count = 0
for i in range(1,n+1):
    if n % i ==0:
        count+=1

    if count == 2:
        print("Yes")
    else:
        print("No")        

n=25
count = 0
for i in range(1,n+1):
    if n % i ==0:
        count+=1

    if count == 2:
        print("Yes")
    else:
        print("No")

#Find if a no is composite no. its is a no, which has more than one factor (excl.1,n). eg 8 = 2,4 = 2 factors

n=8
count=0
for i in range(1,n+1):
    if n % i ==0:
        count+=1
if count > 2:
    print("Yes")
else:
    print("No")            

n=7
count=0
for i in range(1,n+1):
    if n % i ==0:
        count+=1
if count > 2:
    print("Yes")
else:
    print("No")

#Find if a no is Perfect number. A perfect number is equal to sum of its divisors or factors except itself eg 6 = 1 + 2 +3

n=6
sum = 0
for i in range(1,n):
    if n % i ==0:
        sum=sum + i
if sum==n:
    print("Yes")
else:
    print("No")

n=7
sum = 0
for i in range(1,n):
    if n % i ==0:
        sum=sum + i
if sum==n:
    print("Yes")
else:
    print("No")   

#Find if a number is a Abundant no, here sum of factor is greater than the no, itself eg 12. Factors 1,2,3,4,5,6 = 16 > 12

n=12
sum=0
for i in range(1,n):
    if n % i ==0:
        sum=sum+i
if sum > n:
    print("Yes")
else:
    print("No")            

n=6
sum=0
for i in range(1,n):
    if n % i ==0:
        sum=sum+i
if sum > n:
    print("Yes")
else:
    print("No")

#Find if a no is a Deficient no. Sum of factors is less than the no, itself. eg 21. Factors 1,3,7 = 11 < 21

n=21
sum=0
for i in range(1,n):
    if n % i ==0:
        sum=sum+i
if sum < n:
    print("Yes")
else:
    print("No")

n=10
sum=0
for i in range(1,n):
    if n % i ==0:
        sum=sum+i
if sum < n:
    print("Yes")
else:
    print("No")




























































    
       


































