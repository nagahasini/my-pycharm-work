from calendar import month

l=[1,5,6,7,8]
l_2=sorted(l)
l.sort(reverse=True)
#for descending order l.sort(reverse=true)
print(l)
print(l_2)
#**** NOTE: tuple doesnt have .sort so we use sorted


#***Functions**
def fun(*args,**kwargs):
    print(args)
    print(kwargs)

course=['a','b','c']
dic={'a':'hi','b':'hello'}
print(fun(*course,**dic))

months={
    'jan':31,
    'feb':28,
    'march':30
}

def leapyear(year):
    return year%4==0 and year%100!=0 or year%400==0

def numofdays(mon,year):
    if mon not in months:
        return -1
    if mon=='feb' and leapyear(year):
        return 29
    return months[mon]

print(numofdays('feb',2023))


