#average
def average(l):
    add=0
    for i in l:
        add=add+i
    n=len(l)
    return add/n

print(average([1,2,3,4]))

def avg(l):
    return sum(l)/len(l)

a=avg([1,2,3,4])
print(a)
#seperate even and odd
def seperate(l):
    e=[]
    o=[]
    for i in range(len(l)):
        if l[i]%2==0:
            e.append(l[i])
        else:
            o.append(l[i])
    return e,o

lists=[1,2,3,4,5,6,7]
e,o=seperate(lists)
print(e)
print(o)
#smaller elements
def smallerelemets(l,x):
    n=[]
    for i in range(len(l)):
        if l[i]<x:
            n.append(l[i])
    return sorted(n)

print(smallerelemets([3,4,5,2,6,1],5))

#second largest element
def secondlargest(l):
    if len(l)<=1:
        return 0
    largest=l[0]
    secondl=None
    for i in (l[1:]):
        if i>largest:
            secondl=largest
            largest=i
        elif i!=largest:
            if secondl is None or i>secondl:
                secondl=i
    return secondl

print(secondlargest([1,2,3,5,15,22]))

#max in list
def largest(l):
    large=l[0]
    for i in l:
        if i>large:
            large=i
    return large

print(largest([2,3,44,5]))

def reverse(l):
    start=0
    end=len(l)-1
    while start<end:
        l[start], l[end] = l[end], l[start]
        start=start+1
        end=end-1
    return l

print(reverse([1,2,3,3]))

##** remove duplicates
def duplicate(l):
    le=1
    for r in range(1,len(l)):
        if l[r]!=l[r-1]:
            l[le]=l[r]
            le=le+1
    return l[:le]

print(duplicate([1,1,2,2,3]))

#rotate by one
def leftrotate(l):
    l=l[1:]+[l[0]]
    return l
print(leftrotate([1,2,3]))
def lr(l):
    y=l[0]
    for i in range(1,len(l)):
        l[i-1]=l[i]
    l[len(l)-1]=y
    return l
print(lr([1,2,3]))











