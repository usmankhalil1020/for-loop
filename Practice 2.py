
#break

i=1
while i<=5:
    if(i==3):
        break
    i+=1
    print(i)
print("end of loop")

i=1
while i<=6:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop")

i=1
while i<=5:
    if(i==3):
        break
    i+=1
    print(i)
print("end of loop")

i=1
while i<=11:
    print(i)
    if(i==5):
        break
    i+=1
print("end")

num=(1,2,3,4,5,6,7,8,9,10)
x=5
i=0
while i < len(num):
    if(num[i]==x):
        print("found at i :",i)
        break
    else:
        print("finding :")
    i+=1
print("end")

list=[2,1,3,5,4,6,4]
x=4
i=0
while i < len(list):
    if(num[i]==x):
        print("found at i:",i)
        break
    else:
        print("finding :")
    i+=1
print("end")  

list=[1,2,3,4,5,6,7,8,9,10]
x=6
i=0
while i < len(list):
    if(num[i]==x):
        print("found at i :",i)
        break
    else:
        print("finding :")
    i+=1
print("end")

tuple=(2,4,5,3,6,7,4)
x=4
i=0
while i < len(tuple):
    if(tuple[i]==x):
        print("found at i :",i)
        break
    else:
        print("finding :")
    i+=1
print("end")

list=["Usama","Anus","Ahsan","Hasan","Awais"]
x="Hasan"
i=0
while i < len(list):
    if(list[i]==x):
        print("found at i:",i)
        break
    else:
        print("finding :")
    i+=1
print("stop")     

#continue

i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1     

i=0
while i<=10:
    if(i==6):
        i+=1
        continue
    print(i)
    i+=1  

i=0
while i<=12:
    if(i==10):
        i+=1
        continue
    print(i)
    i+=1      

i=0
while i<=15:
    if(i==11):
        i+=1
        continue
    print(i)
    i+=1

i=5
while i>=1:
    if(i==3):
        i-=1
        continue
    print(i)
    i-=1

i=10
while i>=1:
    if(i==7):
        i-=1
        continue
    print(i)
    i-=1

i=11
while i>=0:
    if(i==6):
        i-=1
        continue
    print(i)
    i-=1

i=15
while i>=10:
    if(i==12):
        i-=1
        continue
    print(i)
    i-=1   


i=15
while i>=10:
    print(i)
    if(i==12):
        break
    i-=1
print("end of loop")

i=1
while i<=10:
    if( i % 2==0):
        i+=1
        continue
    print(i)
    i+=1

i=1
while i<=14:
    if(i % 2==0): #even number skip
        i+=1
        continue
    print(i)
    i+=1

i=1
while i<=20:
    if(i % 2==0):
        i+=1
        continue
    print(i)
    i+=1
print("End")

i=10
while i>=0:
    if(i % 2==0):
        i-=1
        continue
    print(i)
    i-=1

i=20
while i>=0:
    if(i % 2==1):
        i-=1
        continue
    print(i)
    i-=1    

i=1
while i<=10:
    if(i % 2!=0):
        i+=1
        continue
    print(i)
    i+=1

i=1
while i<=20:
    if(i % 2!=0):
        i+=1
        continue
    print(i)
    i+=1
    
i=10
while i>=1:
    if(i % 2!=0):
        i-=1
        continue
    print(i)
    i-=1

i=20
while i>=1:
    if(i % 2!=0):
        i-=1
        continue
    print(i)
    i-=1

i=20
while i>=1:
    if(i % 2!=1):
        i-=1
        continue
    print(i)
    i-=1   



















        
        
    











































