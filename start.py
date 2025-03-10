print("hello world")
# to take input from user
name= input("what is your name? ")
print("his name is "+ name)
birth_year=input("enter your birth year: " )
age= 2024-int(birth_year)
print(age)
num1=input("first: " )
num2=input("second: ")
sum= float(num1)+float(num2)
print("sum is  "+ str(sum))
# use str to concatenate
# stringss= strings are immutable
course= "my name is Hasini"
print(course.upper())
print(course.find('y'))
print(course.find('Y'))
print(course.find('name'))
print(course.replace('is','are'))
print('Hasini' in course)

# arithmetic operators
print(10+2)
print(10/2)
# to get integer //
print(10//2)
# 10 to power 3 is
print(10**3)


# comparision operators
# >,>=,==,!=,

# logical operators
price=10
print(price>9 and price<20)
print(price>9 or price<3)
print(not price>20)

# if
temp=int(input("enter temperature"))
if(temp>20):
    print("its hot")

elif(temp<20):
    print("hott ass")

else:
    print("byebye")
print("done")

wt=int(input("enter your weight: "))
unit= input("kg or lbs: ")
if unit=="kg":
    print("weight in lb is "+ str(wt/0.45))

else:
    print("weight in kg is "+str(wt*0.45))

# while loops
i=1
while(i<=5):
    print(i)
    i=i+1

# lists
names=['hi','bye','go']
print(names[0])
names[1]='hello'
# operations such as append,insert,remove(num),clear,len()
print('hi' in names)
print(len(names))

# for loop
numbers=[1,2,3,4]
for i in numbers:
    print(i)

# range
ranges=range(5,10,2)
for i in ranges:
    print(i)

# tuples they are immutable
numberss=(1,2,3,4)
numberss.index(2)


