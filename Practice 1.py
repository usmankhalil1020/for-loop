print("hello world")
print("usman khalil")

a=3
b=9
print(a+b)

print("usman" , "khalil")
print("My name is Usman Khalil","My age is 27")

name="usman khalil"
age=27
print("my name is:",name)
print("My age is:",age)

name="Ibrahim Khalil"
age=22
print("My name is:",name)
print("My age is:",age)

name="Usman Khalil"
Father_Name="Khalil ur Rehman"
Age=26
School="Azeem School"
College="Govt Isl Sci college"
University="Uni of Karachi"

print("My name is:",name)
print("My Father Name is:",Father_Name)
print("My age is:",Age)
print("My School name is:",School)
print("My College name is:",College)
print("My University name is:",University)

age=27
age1=age
print(age1)

fruit="Apple"
fruit1=fruit
print(fruit1)

name="Usman"
age=26
price=34.5
print(type(name))
print(type(age))
print(type(price))


name="Usman"
age=26
price=34.5
print(type(name))
print(type(age))
print(type(price))

age=24
age1=25
age2=26
age3=27
print("Age:",age ,"Age1:",age1,"Age2:",age2,"age3:",age3)

age=27
price=34.45
name="Usman"
old=True
a=None

print(type(age))
print(type(price))
print(type(name))
print(type(old))
print(type(a))

age=27
price=34.45
name="Usman"
old=True
a=None

print(type(age))
print(type(price))
print(type(name))
print(type(old))
print(type(a))

a=7
b=6
sum=a+b
print("The Sum is:",sum)

a=8
b=5
diff=a-b
print("The difference is:",diff)

a=7
b=8
Mul=a*b
print("The product is:",Mul)

a=6
b=3
div=a/b
print("The division is:",div)

a=25
sqr=a**2
print("The square is:",sqr)

a=5
b=2
print("The sum is =",a+b)
print("The difference is =",a-b)
print("The product is =",a*b)
print("The division is =",a/b)
print("The remainder is =",a%b)
print("The square is =",a**b)
print(a==b) #False
print(a!=b) #True
print(a>b)
print(a>=b)
print(a<b) #False
print(a<=b) #False


num=10
num1=num + 10
print(num1)

num=20
num1=num + 20
print("The req no is =",num1)

num=30
num+=10
num-=10
num*=10
num/=10
num**=10
num%=10
print("num:",num)

a=30
b=20
print(not True) #False
print(not (a>b)) #False

a=76
b=90
print(not True) #False
print(not False) #True
print(not (a>b)) #True

val1=True
val2=True
print("and operator", val1 and val2)
print("or operator", val1 or val2)

val1=True
val2=False
print("and operator", val1 and val2) #False
print("or operator", val1 or val2) #True

a=30
b=20
print("or operator",(a==b) or (a>b)) #True
print("and operator", (a==b) and (a>b)) #False

#Type Conversion
a=4
b=2.5
print("The sum is =",a+b)

#Type Casting
a=int("4")
b=2.5
print(type(a))
print(a+b)

a=int("6")
b=float("6.5")
print(a+b)
print(type(a))
print(type(b))

a=3.14
a=str(a)
print(type(a)) #string

name = input("enter your name:")
print("welcome",name)

name=input("enter your name:")
print("welcome:",name)
age=input("enter your age:")
print("your age is:",age)

val=input("enter your values:")
print(type(val),val)

num=int(input("enter your num:"))
print(type(num),num)

num=float(input("enter your number:"))
print(type(num),num)

name=input("enter your name:")
age=int(input("enter your age:"))
marks=float(input("enter your marks:"))

name=input("enter your name:")
age=int(input("enter your age:"))
marks=float(input("enter your marks:"))

print("welcome",name)
print("your age is=",age)
print("your marks is=",marks)

name=input("enter your name:")
age=int(input("enter your age:"))
marks=float(input("enter your marks:"))

first=int(input("first number:"))
second=int(input("second number:"))
print("sum=",first + second)

first=float(input("enter first number:"))
second=float(input("enter second number:"))
third=float(input("enter third number:"))
print("sum =",first+second+third)


first=int(input("first number:"))
second=int(input("second number:"))
third=int(input("third number:"))
print("difference =",first-second-third)

str1="My name is usman.\nI am good in python"
print(str1)

str1="My name is Usman Khalil.\nI am good in python"
print(str1)

str1="My name is Usman Khalil.\tI am good in python"
print(str1)

str="My name is Usman Khalil.\tI am good in English.\tI am good in English."
print(str)

str="University"
l=len(str)
print(l)

str="University of Karachi"
print("The length of string is =",len(str))
str1="Sir Syed University"
print(len(str1))
final_str=str+" "+str1
print("Final string is:",final_str)
print("Length of final string is =",len(final_str))

str="Karachi University"
cha=str[5]
print(cha)

str="University"
cha=str[6]
print("Character of this string is:",cha)

str="karachi university"
print(str[8])

str="karachi university"
print(str[1:4])
print(str[0:4])
print(str[0:7])
print(str[0:9])

str="karachi university"
print(str[7:len(str)])
print(str[8:len(str)])
print(str[9:len(str)])

str="usman"
print(str[-3])
print(str[-3:-1])

str="üniversities"
slicing=str[-7:-1]
print(slicing)

str="University of karachi"
slicing=str[-8:-3]
print(slicing)

str="I am studying python from University of kkarachi"
print(str.endswith("chi"))
print(str.endswith("opo"))
print(str.endswith("ity"))

str="Usman"
print(str.endswith("an"))
print(str.endswith("on"))

str="usman"
print(str.capitalize())

str="i am studying"
print(str.capitalize())
print(str)

str="i am studying"
str1=str.capitalize
print(str1())

str="I am studying from university of karachi"
print(str.replace("r","o"))
print(str.replace("y","Y"))
print(str.replace("a","A"))

str="I am studying python from ku"
print(str.replace("python","java"))
print(str.replace("am studying","have studied"))

str="I am"
print(str.find("a"))

str="Usman Khalil"
print(str.find("h"))
print(str.find("i"))
print(str.find("l"))

str="I am from studying python from ku from sir syed"
print(str.count("from"))
print(str.count("from"))

str="Usmann"
print(str.count("n"))

name=input("enter your name:")
print("length of name =",len(name))

password=input("enter your password")
print("length of password is =",len(password))

length=input("enter length")
breath=input("enter breath")
print("length =",length)
print("breath",breath)

a=int(input("enter first number"))
b=int(input("enter second number"))
print("Average of two numbers is =",a+b/2)

str="$i am $ from ku $"
print("No of $ is =",str.count("$"))

light=input("Light color")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("start")
elif(light=="green"):
    print("run")    

marks=int(input("enter your marks"))
if marks > 90:
    print("A+")
elif marks < 90 and marks > 80:
    print("A")
elif marks < 80 and marks > 70:
    print("B+")
elif marks > 70 and marks < 60:
    print("B")
else:
    print("C") 

age=24
if age>=18:
    print("can vote")
else:
    print("cannot vote")

light="pink"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("run")
else:
    print("break")

num=25
if(num > 25):
    print("greater than 25")
elif(num < 25):
    print("less than 25")

age=45
if(age<18 and age>60):
    print("cannot drive")
else:
    print("can drive") 

num=int(input("enter number:"))
if(num % 2==0):
    print("even")
else:
    print("odd")   


num=int(input("enter number:"))
rem=num % 2
if(rem == 0):
    print("Even")
else:
    print("Odd")

a=int(input("first no"))
b=int(input("Second no"))
c=int(input("third no"))

if(a>=b and a>=c):
    print("first no is largest")
elif(b>=c):
    print("second no is largest")
else:
    print("third no is largest")

a=int(input("first no"))
b=int(input("second no"))
c=int(input("third no"))
d=int(input("forth no"))

if(a>=b and a>=c and a>=c):
    print("first no is largest")
elif(b>=c and b>=d):
    print("second no is largest")
elif(c>=d):
    print("third no is largest")
else:
    print("forth no is largest")

a=int(input("enter number"))
if(a % 7==0):
    print("Multiples of 7")
else:
    print("not multiples of 7")

b=int(input("enter number"))
if(b % 5==0):
    print("multiples of 5")
else:
    print("not multiples of 5")                        

marks=[23,45,67,76,54,67,87,87]
print("markks",marks)
print("length of marks =",len(marks))
print("Type",type(marks))
print(marks[0])
print(marks[2])

Student=["Usman",55.5,56,"karachi"]
print(Student[0])
Student[0]="Ibrahim"
print(Student)

Student=["Usman",45.5,45,"Ibrahim"]
print(type(Student))
print(type(Student[1]))
Student[0]="Asma"
print(Student)

marks=[34,56,76,89,76,56,55]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])
print(marks[-4:-1])

list=[3,4,5,6,5.4]
list.append(9)
print(list)

list=[3,4,5,6,7]
list.append(10)
print(list)

list=[2,3,5,4,3,7]
list.sort()
print(list)

list=[12,34,54,32,45,67]
print(list.sort())
print(list)

list=[34,33,23,67,45]
list.append(90)
list.sort()
print(list)

list=[2,3,2,5,4,6,7]
print(list.sort(reverse=True))
print(list)

list=[2,3,4,3,2,7,5,8,6,9]
print(list.sort(reverse=True))
print(list)

list=["apple","mango","banana","orange"]
list.append("Ladyfinger")
list.sort()
print(list.sort(reverse=True))
print(list)

list=["a","b","c","d","e"]
list.reverse()
print(list)

list=[1,2,3,4,5,6]
list.insert(7,8)
list.insert(7,9)
print(list)

list=[1,2,3]
list.insert(5,4)
list.insert(4,5)
print(list)

list=[1,2,3,4,5]
list.pop(3)
print(list)

list=[1,2,3,4,5,6,7]
list.pop(6)
print(list)

list=[]
print(list)
print(type(list))

#Tuple

tuple=(3,4,3,5,6,7,3,8)
print(type(tuple))
print(tuple[0])
print(tuple[3])

tuple=()
print(tuple)
print(type(tuple))

tuple=(1,)
print(tuple)
print("Type:",type(tuple))

tuple=(1,2,3,4,5,6)
print(tuple[1:3])
print(tuple[0:1])

tuple=(1,3,4,5,4,7,8)
print(tuple.index(4))
print(tuple.count(4))

movies=[]

movie1=input("enter first movie")
movie2=input("enter second movie")
movie3=input("enter third movie")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)

list=[]

list1=int(input("enter first no"))
list2=int(input("enter second no"))
list3=int(input("enter third no"))

list.append(list1)
list.append(list2)
list.append(list3)

print(list)

fruit=[]

fruit1=input("enter first fruit")
fruit2=input("enter second fruit")
fruit3=input("enter third fruit")

fruit.append(fruit1)
fruit.append(fruit2)
fruit.append(fruit3)

print(fruit)

even=[]

even.append(int(input("enter first even no:")))
even.append(int(input("enter second even no:")))
even.append(int(input("enter third even no:")))

print(even)

fruit=[]

fruit.append(input("enter first fruit name:"))
fruit.append(input("enter second fruit no:"))
fruit.append(input("enter third fruit no:"))

print(fruit)

#Pallintrome

list=[1,2,1]

copy_list=list.copy()
copy_list.reverse()
if(copy_list==list):
    print("pallintrome")
else:
    print("not pallintrome")

list=[2,1,2]

copy_list=list.copy()
copy_list=list.reverse()
if(copy_list==list):
    print("pallintrome")
else:
    print("not a pallintrome") 

grade=("a","b","c","a")
print(grade.count("a"))    

grade=("a","b","c","a")
grade.count("a")
print(grade)

info={
    "name":"Usman",
    "key":"value",
    "University":"ku"
}

print(info)

info={
    "name":"Usman Khalil",
    "School":"Azeem School",
    "College":"Govt Isl Sci College"
}

print(info)

#Dictionary

info={
    "name":"Usman Khalil",
    "Father":"Khalil ur Rehman",
    "age":"24",
    "school":"Azeem School",
    "Is adult":True
}

print(info)
print(type(info))

info={
    "name":"Usman Khalil",
    "Father":"Khalil ur Rehman",
    "age":"24",
    "school":"Azeem School",
    "age":24

}

info["name"]="Ibrahim"
info["Surname"]="Khalil"

print(info["name"])
print(info["Surname"])

nfo={
    "name":"Usman Khalil",
    "Father":"Khalil ur Rehman",
    "age":"24",
    "school":"Azeem School",
    "age":24

}

info["name"]="Asma"
info["age"]=25

print(info["name"])
print(info["age"])

null_dict={}
null_dict["name"]="Sir syed"
print(null_dict)

null_dict={}
null_dict["name"]="Usman"
null_dict["Profession"]="Teaching"
null_dict["Age"]=26
null_dict["Nick Name"]="Ibrahim"
print(null_dict)

#Nested Dictionary

Student={
    "Names":{
        "Usman":67,
        "Asma":87
    },

    "Subjects":{
        "phy":98,
        "Chem":76,
        "Math":89
    }

}

print(Student)
print(Student["Subjects"]["Chem"])
print(Student["Names"])

Student={
    "namees":{
        "usman":87,
        "Ahsan":76,
        "Uzair":54
    },

    "Subjects":{
        "phy":54,
        "che":69,
        "math":34
    },

    "Mobiles":{
        "Infinix":50000,
        "oppo":20000,
        "samsung":60500
    }
}

print(Student)
print(Student["Mobiles"]["oppo"])
print(Student["namees"]["usman"])
print(Student["namees"])
print(Student["Subjects"])

Student={
    "names":{
        "usman":65,
        "asma":78,
        "ifra":73
    },

    "subjects":{
        "phy":47,
        "chem":71,
        "math":58
    },

    "Mobiles":{
        "infinix":20000,
        "oppo":60000,
        "samsung":90000
    }
}

print(Student)
print(Student["names"])
print(Student["subjects"])
print(Student["Mobiles"])

print(Student["names"]["asma"])
print(Student["subjects"]["math"])
print(Student["Mobiles"]["oppo"])

#Methods of dictionary

Student={
    "names":"usman",
    "subjects":{
        "phy":65,
        "chem":65,
        "math":87
    },

    "roll no":306356,
    "gpa":2.8
  

}

print(Student)
print(Student["names"])
print(Student["subjects"])
print(Student["subjects"]["math"])
print(Student["roll no"])
print(Student["gpa"])

Student={
    "names":"usman",
    "subjects":{
        "phy":56,
        "chem":87
    }
}

print(Student.keys())
print(Student.values())
print(Student.items())
print(Student["names"])
print(Student.get("names"))
print(Student.get("subjects"))

Student={
    "names":"usman",
    "subjects":{
        "phy":65,
        "che":85,
        "math":85
    }
}

new_dict={"city":"karachi","age":27}
Student.update(new_dict)
print(Student)

Student={
    "names":{
        "usman":25,
        "asma":54
    },
    "subjects":{
        "phy":65,
        "chem":75
    },
    "roll no":306356
}

new_dict={"city":"karachi","age":26}
Student.update(new_dict)
print(Student)

Student={
    "names":"Usman Khalil",
    "subjects":{
        "phy":58,
        "chem":65   
    },
    "roll no":326547,
    "Gr No":212165
}

new_dict={"city":"Lahore","age":29}
Student.update(new_dict)
print(Student)

#Sets

set={1,2,3,"usman",4,6}
print(set)
print(type(set))
print(len(set))  #total no of items

set={1,2,3,4,"usman","keys"}
print(set)
print(type(set))
print(len(set))

info={
    "name":"Usman",
    "key":"value",
    "University":"ku"
}

print(info)

info={
    "name":"Usman Khalil",
    "School":"Azeem School",
    "College":"Govt Isl Sci College"
}

print(info)

#Dictionary

info={
    "name":"Usman Khalil",
    "Father":"Khalil ur Rehman",
    "age":"24",
    "school":"Azeem School",
    "Is adult":True
}

print(info)
print(type(info))

info={
    "name":"Usman Khalil",
    "Father":"Khalil ur Rehman",
    "age":"24",
    "school":"Azeem School",
    "age":24

}

info["name"]="Ibrahim"
info["Surname"]="Khalil"

print(info["name"])
print(info["Surname"])

nfo={
    "name":"Usman Khalil",
    "Father":"Khalil ur Rehman",
    "age":"24",
    "school":"Azeem School",
    "age":24

}

info["name"]="Asma"
info["age"]=25

print(info["name"])
print(info["age"])

null_dict={}
null_dict["name"]="Sir syed"
print(null_dict)

null_dict={}
null_dict["name"]="Usman"
null_dict["Profession"]="Teaching"
null_dict["Age"]=26
null_dict["Nick Name"]="Ibrahim"
print(null_dict)

#Nested Dictionary

Student={
    "Names":{
        "Usman":67,
        "Asma":87
    },

    "Subjects":{
        "phy":98,
        "Chem":76,
        "Math":89
    }

}

print(Student)
print(Student["Subjects"]["Chem"])
print(Student["Names"])

Student={
    "namees":{
        "usman":87,
        "Ahsan":76,
        "Uzair":54
    },

    "Subjects":{
        "phy":54,
        "che":69,
        "math":34
    },

    "Mobiles":{
        "Infinix":50000,
        "oppo":20000,
        "samsung":60500
    }
}

print(Student)
print(Student["Mobiles"]["oppo"])
print(Student["namees"]["usman"])
print(Student["namees"])
print(Student["Subjects"])

Student={
    "names":{
        "usman":65,
        "asma":78,
        "ifra":73
    },

    "subjects":{
        "phy":47,
        "chem":71,
        "math":58
    },

    "Mobiles":{
        "infinix":20000,
        "oppo":60000,
        "samsung":90000
    }
}

print(Student)
print(Student["names"])
print(Student["subjects"])
print(Student["Mobiles"])

print(Student["names"]["asma"])
print(Student["subjects"]["math"])
print(Student["Mobiles"]["oppo"])

#Methods of dictionary

Student={
    "names":"usman",
    "subjects":{
        "phy":65,
        "chem":65,
        "math":87
    },

    "roll no":306356,
    "gpa":2.8
  

}

print(Student)
print(Student["names"])
print(Student["subjects"])
print(Student["subjects"]["math"])
print(Student["roll no"])
print(Student["gpa"])

Student={
    "names":"usman",
    "subjects":{
        "phy":56,
        "chem":87
    }
}

print(Student.keys())
print(Student.values())
print(Student.items())
print(Student["names"])
print(Student.get("names"))
print(Student.get("subjects"))

Student={
    "names":"usman",
    "subjects":{
        "phy":65,
        "che":85,
        "math":85
    }
}

new_dict={"city":"karachi","age":27}
Student.update(new_dict)
print(Student)

Student={
    "names":{
        "usman":25,
        "asma":54
    },
    "subjects":{
        "phy":65,
        "chem":75
    },
    "roll no":306356
}

new_dict={"city":"karachi","age":26}
Student.update(new_dict)
print(Student)

Student={
    "names":"Usman Khalil",
    "subjects":{
        "phy":58,
        "chem":65   
    },
    "roll no":326547,
    "Gr No":212165
}

new_dict={"city":"Lahore","age":29}
Student.update(new_dict)
print(Student)

#Sets

set={1,2,3,"usman",4,6}
print(set)
print(type(set))
print(len(set))  #total no of items

set={1,2,3,4,"usman","keys"}
print(set)
print(type(set))
print(len(set))






collection=set()
collection.add(1)
collection.add(2)
collection.add(3)

print(collection)

value=set()
value.add(4)
value.add(8)
value.add(16)

print(value)

value=set()

value.add(1)
value.add(3)
value.add(7)
value.add(5)
value.remove(7)
value.add("usman")
value.add((1,2,3))

print(value)

value=set()

value.add(2)
value.add(4)
value.add(7)
value.add(("A","B","C"))
value.remove(7)
value.clear()  #0

print(value)
print(len(value))

names=("usman","umar","asma","samra")
print(names.count("usman"))

names={"usman","umar","ibrahim","asma","samra"}
print(names.pop())
print(names.pop())
print(names.pop())

list=[1,2,3,4,5,6]
print(list.pop())
print(list.pop())
print(list.pop())

#Union, intersection, difference and symmetric difference

set1={1,2,3,4}
set2={3,4,5,6}
print("Union",set1.union(set2))
print("Intersection",set1.intersection(set2))
print("difference",set1.difference(set2))
print("Symmetric difference",set1.symmetric_difference(set2))

set1={1,2,3}
set2={4,5,6,7}
set3={6,7,8,9}

print(set1.union(set2,set3))
print(set1.intersection(set2,set3))
print(set1.difference(set2,set3))
print(set1.symmetric_difference(set3))

dict={
    "cat":"a small animal",
    "table":["a place of furniture","list of fact and figures"]
}

print(dict)

names={"names":["usman","umar","asma"]}
print(names)

dict={
    "names":"usman khalil",
    "subjects":["what do you know about subjects","introduce your self"]
}

print(dict)

Student={
    "names":"usman khalil",
    "subjects":["physics chemistry and maths","english urdu and pst"]
}

print(Student)

Subjects={
    "python","java","C++","python","digital marketing","javascript","java","graphic designing","java","javascript"
}

print(Subjects)
print("length of Subjects =",len(Subjects))

marks={}

x=int(input("enter phy:"))
marks.update({"phy":x})

y=int(input("enter math:"))
marks.update({"math":y})

z=int(input("enter che:"))
marks.update({"che":z})

print(marks)

marks={}

x=int(input("enter phy:"))
marks.update({"phy":x})

y=int(input("enter math:"))
marks.update({"math":y})

z=int(input("enter che:"))
marks.update({"che":z})

t=int(input("enter eng:"))
marks.update({"eng":t})

print(marks)


fruits={}

a=input("enter first fruit:")
fruits.update({"first fruit":a})

b=input("enter second fruit:")
fruits.update({"second fruit":b})

c=input("enter third fruit:")
fruits.update({"third fruit":c})

print(fruits)

even_no={}

x=int(input("enter first even no:"))
even_no.update({"first even no":x})  

y=int(input("enter second even no:"))
even_no.update({"second even no":y})

z=int(input("enter third even no:"))
even_no.update({"third even no":z})

print(even_no)


value={9,9,0}
print(value)


val={9,9,0}
print(val)

val={9,9,25}
print(val)

val={1,2,1,1,4,5}
print(val)

val={9,9.25,8,8.0}
print(val)

val={9,9.0}
print(val)

val={
    ("float",9.0),
    ("str","usman"),
    ("int",65)
}

print(val)

info={
    ("name","usman"),
    ("father name","khalil ur rehaman"),
    ("roll no",306356),
    ("subject",("maths"),("physics"))
}

print(info)

info={
    ("name","usman khalil"),
    ("father name","khalil ur rehman"),
    ("roll no",306356,6958),
    ("Subjects",("maths",65),("physics",74))
}

print(info)

#Loops
#While loop

count=1
while count<=5:
    print("usman")
    count+=1

count=1
while count<=10:
    print("run")
    count+=1   

i=1
while i<=5:
    print("Go")
    i+=1

run=1
while run<=5:
    print("run fast")
    run+=1

i=1
while i<=5:
    print(i,5)
    i+=1 

i=1
while i<=5:
    print(i,"usman khalil")
    i+=1

i=1
while i<=5:
    print("usman",i) 
    i+=1

a=1
while a<=5:
    print(a,"usman khalil")
    a+=1

i=1
while i<=5:
    print(i,"A","B","C","D")
    i+=1

i=1
while i<=5:
    print(i)
    i+=1
print("end loop") 

i=1
while i<=6:
    print(i,"usman")
    i+=1
print("End")

i=1
while i<=6:
    print(i,"Go")
    i+=1
print("stop")

#print numbers from 1 to 100

i=1
while i<=100:
    print(i)
    i+=1

#print numbers from 100 to 1

i=100
while i>=1:
    print(i)
    i-=1

#print multiplication table

i=1
while i<=10:
    print(3*i)
    i+=1

i=10
while i>=1:
    print(3*i)
    i-=1  

i=1
while i<=10:
    print(4*i)
    i+=1

i=10
while i>=1:
    print(4*i)
    i-=1

n=int(input("enter number"))
i=1
while i<=10:
    print(n*i)
    i+=1
    
n=int(input("enter number"))
i=1
while i<=10:
    print(n*i)
    i+=1

n=int(input("enter even no"))
i=1
while i<=10:
    print(n*i)
    i+=1 

n=int(input("enter number:"))
i=10
while i>=1:
    print(n*i)
    i-=1     
#Index

num=[1,4,9,16,25,36,49,64,81,100]
index=0
while index < len(num):
    print(index)
    index+=1     

num=[1,2,3,4,5,6]
index=0
while index < len(num):
    print(index)
    index+=1 

list=[1,2,3,4,5,6,7,8,9]
index=0
while index < len(list):
    print(index)
    index+=1    

str=["usman","asma","ibrahim"]
index=0
while index < len(str):
    print(index)
    index+=1 

num=[34,34,55,78,55,67,65,66,5,44,78]
index=0
while index < len(num):
    print(index)
    index+=1


#while loop

i=1
while i<=5:
    print(i,"usman")
    i+=1

print("loop end")

i=5
while i>=1:
    print(i,"usman")
    i-=1
print("end loop")

i=10
while i>=0:
    print(i,"usman")
    i-=1
print("end")

i=5
while i>=-5:
    print(i,"usman khalil")
    i-=1
print("end")

#print numbers from 1 to 100

i=1
while i<=100:
    print(i)
    i+=1

#print multiplication table of a number n

i=1
while i<=10:
    print("3*",i,"=",3*i)
    i+=1

i=1
while i<=10:
    print("4*",i,"=",4*i)
    i+=1

i=1
while i<=10:
    print("5*",i,"=",5*i)
    i+=1

#Index

list=[1,2,3,4,5,6,7,8,9]
index=0
while index < len(list):
    print(index)
    index+=1       

list=[1,2,3,4,5,6,7]
index=0
while index < len(list):
    print(index)
    index+=1

list=["usman","umar","asma"]
index=0
while index < len(list):
    print(index)
    index+=1 

#Print the elements of the list using a loop

nums=[1,4,9,16,25,36,49,64,81,100]
index = 0
while index < len(nums):
    print(nums[index])
    index+=1


nums=[1,4,9,16,25,36,49,64,81,100]
index = 0
while index < len(nums):
    print(nums[index])
    index+=1      

list=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(list):
    print(i,list[i])
    i+=1 

#traverse
nums=[1,4,9,16,25,36,49,64,81,100]
index = 0
while index < len(nums):
    print(index,nums[index])
    index+=1

names=["usman","umar","ibrahim","asma"]
index=0
while index<len(names):
    print("Name :",index,names[index])
    index+=1

names = ["samra","asma","usman","umar","ibrahim","saad","kinza","kiran","abdullah","ismael"]
index=0
while index < len(names):
    print("Name :",index,names[index])
    index+=1

#Search for a number x in this tuple using loop

nums=(1,4,9,16,25,36,49,64,81,100) 

x=36

index=0
while index < len(nums):
    if(nums[index] == x):
        print("found at index :",index)
    else:
        print("finding")    
    index+=1


nums=(1,4,9,16,25,36,49,64,81,100,64) 
x=64
index=0
while index < len(nums):
    if(nums[index] == x):
        print("found at index",index)
    else:
        print("finding")
    index+=1        

fruits=("apple","banana","orange","watermelon","grapes")
x="orange"
index=0
while index<len(fruits):
    if(fruits[index]==x):
        print("found at index",index)
    else:
        print("finding")
    index+=1

nums=(1,2,3,4,2,5,6,2,7,8,9)
x=2
index=0
while index<len(nums):
    if(nums[index]==x):
        print("index",nums[index])
    index+=1

nums=(1,2,3,4,2,3,2,5,6,7,8)
x=2
index=0
while index<len(nums):
    if(nums[index]==x):
        print("found in",index)
    else:
        print("finding")    
    index+=1

nums=(1,2,3,4,2,3,2,5,6,7,8)
x=4
index=0
while index<len(nums):
    if(nums[index]==x):
        print("index at",index)
    else:
        print("finding")    
    index+=1

#Break statement

i=1
while i<=5:
    print(i)
    if i==4:
        break
    i+=1
print("end")

i=1
while i<=10:
    print(i)
    if i==5:
        break
    i+=1
print("END")

i=1
while i<=20:
    print(i)
    if i==15:
        break
    i+=1
print("ENd")

list=[1,4,9,16,25,36,49,64,81,100,36]
x=36
i=0
while i<len(list):
    if(list[i]==x):
        print("found at",i)
        break
    else:
        print("finding")
    i+=1
print("end")   


 


list=[1,4,9,16,25,36,49,64,81,100,36]
x=36
i=0
while i<len(list):
    if(list[i]==x):
        print("found at",i)
        break
    else:
        print("finding")
    i+=1
print("end")  

list=[1,4,9,16,25,36,49,64,81,100,36]
x=36
i=0
while i<len(list):
    if(list[i]==x):
        print("found at idx",i)
        break
    else:
        print("finding")
    i+=1

list=[1,4,9,16,25,36,49,64,81,100,64,64]
x=64
i=0
while i<len(list):
    if(list[i]==x):
        print("found at idx",i)
        break
    else:
        print("finding")    
    i+=1    

list=[1,4,9,16,64,36,49,64,81,100,64,64]
x=64
i=0
while i<len(list):
    if(list[i]==x):
        print("found at idx",i)
        break
    else:
        print("finding")    
    i+=1

list=[1,4,64,16,64,36,49,64,81,100,64,64]
x=64
i=0
while i<len(list):
    if(list[i]==x):
        print("found at idx",i)
        break
    else:
        print("finding")    
    i+=1

#Continue

i=1
while i<=5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1    

i=0
while i<=5:
    if(i==4):
        i+=1
        continue
    print(i)
    i+=1    

i=5
while i>=1:
    if i==3:
        i-=1
        continue
    print(i)
    i-=1    

i=0
while i<=10:
    if(i==5):
        i+=1
        continue
    print(i)
    i+=1

i=10
while i>=0:
    if(i==6):
        i-=1
        continue
    print(i)
    i-=1

i=1
while i<=10:
    if(i==7):
        i+=1
        break
    print(i)
    i+=1    

i=10
while i>=1:
    if(i==5):
        print(i)
        break
    print(i)
    i-=1  

i=1
while i<=10:
    if(i==6):
        i+=1
        continue
    print(i)
    i+=1  

i=10
while i>=0:
    if(i==7):
        i-=1
        continue
    print(i)
    i-=1  

list=[1,4,9,16,64,36,49,64,81,100,64,64]
x=64
i=0
while i<len(list):
    if(list[i]==x):
        print("found at idx",i)
        break
    else:
        print("finding")    
    i+=1  

i=1
while i<=10:
    if(i % 2==0):
        i+=1
        continue
    print(i)
    i+=1

i=1
while i<=10:
    if(i % 2==0):
        i+=1
        continue
    print("odd no",i)
    i+=1    

i=1
while i<=10:
    if(i % 2 ==1):
        i+=1
        continue
    print("even no",i)
    i+=1  

i=1
while i<=20:
    if(i % 2==0):
        i+=1
        continue
    print("odd no",i)
    i+=1

i=1
while i<=20:
    if(i % 2==1):
        i+=1
        continue
    print("Even no",i)
    i+=1  

i=20
while i>=1:
    if(i % 2==0):
        i-=1
        continue
    print("odd no",i)
    i-=1     

i=20
while i>=1:
    if(i % 2!=1):
        i-=1
        continue
    print("odd no",i)
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

#For loop

list=[1,2,3,4,5]

for val in list:
    print("Number",val)
print(type(list))

list=(2,3,4,5,6,7,8,9)
for val in list:
    print(val)   
print(type(list))

set={1,2,3,4,5,6}
for val in set:
    print(val)
print(type(set))

str="usmankhalil"
for char in str:
    print(char)

str="usman"
for char in str:
    print(char)

list=[1,2,3,4,5,6,7,8,9]

for val in list:
    if val % 2==0:
        print("Even no",val)

list=[1,2,3,4,5,6,7,8,9,10]

for val in list:
    if val % 2!=0:
        print(val)

list=[1,2,3,4,5,6,7,8,9,10]  

for val in list:
    if val % 2!=1:
        print(val)

str="usman"
for char in str:
    print(char)
else:
    print("end")

str=["usman"]
for char in str:
    str.append(char)   
     





































































































































































































































   














































































































































































    


        





















      




















































































































































































































































































































































































































































































































































































































































