import datetime


s=['hey','u']
sen="hello {0[0]} there{0[1]}".format(s)
name=input("enter:")
age=input("age: ")
print(f"my name is{name}and age id{age}")
ss={'age':18,'name':'apa'}
print("name is {1} and age is{0}".format(ss['age'],ss['name']))
###3for dictionary
print("my name is{name} and age is{age}".format(**ss))
pi=3.1255
print("value is {:.2f}".format(pi))

#DOCSTRINGS
print(pow(5,2))

####formatting date
tdy=datetime.datetime.today()
print("today is{0:%B,%d,%Y} and day is{0:%A}".format(tdy))

##SET
s={1,'verv',333,'f'}
print(s)
s={1,2,3}
a={5,6}
s.update(a)#a values go to s

def fun(num):
    '''here is num '''
    if num%2==0:
      print(fun.__doc__)
fun(4)