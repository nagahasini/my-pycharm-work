from operator import truediv
from pickle import FALSE

print(ord("a"))
print(chr(97))

#### STRINGS ARE IMMUTABLE ####### i.e s[0]=e gives error

# MULTI LINE STRINGS
a= ''' hello
"hasini"
hey there
'''
print(a)
print('hi\nhello')

#ESCAPE SEQUENCE
b='Hi there this is hasini\'s code'
print(b)

# to print \n we use \\n

#  RAW STRINGS
s2=r"c:project\name"

# FORMATTED STRING
name='hasini'
course='python'
s3= f'hello {name} welcome to {course} course'
print(s3)
a=1
b=2
print( f"sum od {a} and {b} is {a+b}")
a1='ABC'
a2='abc'
print(f'lower of {a1} is {a1.lower()}')
print(f'upper of {a2} is {a2.upper()}')

# STRING COMPARISIONS
s1='girl'
s4='ilu'
print(s1<s4)
print('ABC'>'abc')  #false as a is 97


#  STRING OPERATIONS

h='hasinirepaka hasini'
g='hasini'    ##substring
print(g in h)
print(g not in h)

#concatenate
print(h+g+'is my name')
#indexs
print(h.index(g))
print(h.rindex(g))

#length
print(len(g)) #return no of chars

print(h.startswith('hasini'))
print(g.endswith('hasini'))

print(h.startswith('re',6,len(h))) #index 6 is start of repaka's r

## SPLIT AND JOIN
e='hello there how are you'
print(e.split())
e2= 'hello,there you'
print(e2.split(','))

l=['hello','there','you']
print(''.join(l))
print(','.join(l))

## STRIP
st= '------- hasini -----'
print(st.strip('-'))
print(st.rstrip('-'))

##### FIND METHOD (similar to index but doesnt give error)
print(h.find(g)) #we get 0
print(h.find(g,2,len(h)))

# REVERSE
p=input("enter string")
print(p[::-1])

##Check for rotation
def are_rotations(x,y):  #0(N)
    if len(x)!=len(y):
        return False
    temp=''
    temp=x+x
    return temp.find(x)!=-1

print(are_rotations('abcd','dbca'))

def is_palindrome(q):
    if len(q)==1:
        return True
    if q[::-1]==q:
        return True
    else:
        return False

print(is_palindrome('abc'))

### Check if a string is Subsequence of other *** ex: for abcdef  ade is subseq, its not necessary to be continous
def is_subseq(u,v): ##0(N)
    i,j=0,0
    while i<len(u) and j<len(v):
        if u[i]==v[j]:
            j+=1
        i+=1
    return j==len(v)

print(is_subseq('abcd','abd'))

#recursive way of doing this is

def iss_subsequence(j,k,d,q):
    if q==0:
        return True
    if d==0:
        return False
    if j[d-1]==k[q-1]:
        return iss_subsequence(j,k,d-1,q-1)
    else:
        return iss_subsequence(j,k,d-1,q)

print(iss_subsequence('abcd','ca',4,2))

## CHECK for Anagraam. in the both strings same letter appears same time

def anagramcheck(h1,h2):     #0(N)
    if len(h1)!=len(h2):
        return False

    count=[0]*256
    for i in range(0,len(h1)):
        count[ord(h1[i])]+=1
        count[ord(h2[i])] -= 1

    for x in count:
        if x!=0:
            return False

    return True

print(anagramcheck('aabc','acab'))

# LEFTMOST REPEATING   for abccb the first b is answerof it

#first approach :O(N)

def leftmost1(string1):
    ind= [-1]*256
    res=float('-inf')
    for i in range(len(string1)):
        if ind[ord(string1[i])]==-1:
            ind[ord(string1[i])]=i
        else:
            res=max(res,ind[ord(string1[i])])
    return res

arey=leftmost1('aba')
print(arey)

#second approach
def leftmost2(string2):
    visited=[False]*256
    ress=-1
    for i in range(len(string2)-1,-1,-1):
        if visited[ord(string2[i])]:
            ress=i
        else:
            visited[ord(string2[i])] = True
    return ress

areyy=leftmost2('aba')
print(arey)



# LEFTMOST NON REPEATING
def leftmostnon_repeating(stringg):
    l_s=[-1]*256
    for i in range(len(stringg)):
        if l_s[ord(stringg[i])]==-1:
            l_s[ord(stringg[i])]=i
        else:
            l_s[ord(stringg[i])] = -2
    res1=float('inf')
    for x in l_s:
        if  x>=0:
            res1=min(res1,x)
    if res1==float('inf'):
        return -1

    return res1

areyyy=leftmostnon_repeating('aba')
print(areyyy)

#reverse words in string
def reverse(string3):
    words=string3.split(" ")
    words=[w[::-1] for w in words]
    string3=" ".join(words)
    return string3[::-1]

stringg3='hi there '
r=reverse(stringg3)
print(r)

def reverse_regular(string4,beg,end):
    while beg<end:
        string4[beg],string4[end]=string4[end],string4[beg]
        beg+=1
        end-=1

def rev(s):
    s=list(s)
    beg1=0
    n=len(s)
    for i in range(n):
        if s[i]==' ':
            reverse_regular(s,beg1,i-1)
            beg1=i+1


    reverse_regular(s,beg1,n-1)
    reverse_regular(s,0,n-1)
    return ''.join(s)

print(rev('hello everybody'))



























