from idlelib.sidebar import temp_enable_text_widget
from itertools import count
#
#
# def gcd(a,b):
#     if b==0:
#         return a
#
#     return gcd(b,a%b)
#
#
# print(gcd(12,15))
# print(gcd(2,20))
#
# def prime(n):
#     count = 0
#     for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to square root of n
#         if n % i == 0:
#             count += 1
#             break  # No need to continue if we find a divisor
#
#     if count==0:
#         return True
#     else:
#         return False
#
# print(prime(4))
#
# def primefactors(n):
#
#     for i in range(2,n):
#         if n%i==0 and prime(i):
#             x=i
#             while n%x==0:
#              print(i)
#              x=x*i
#
# print(primefactors(36))
#
# def alldivisors(n):
#      i=1
#      while(i*i<n):
#          if n%i==0:
#              print(i)
#          if i!=n//i:
#           print(n//i)
#          i=i+1
#
# print(alldivisors(20))

#seive of eras
def eras(n):
    p=[0 for i in range(n+1)]
    for i in range(2,n+1):
        if p[i]==0:
            for j in range(i*i,n+1,i):
                p[j]=1
    for i in range(2,n+1):
        if p[i]==0:
            print(i)

eras(10)

#computing power
def power(x,n):
    if n==0:
        return 1
    temp=pow(x,n//2)
    temp=temp*temp
    if n%2==0:
        return temp
    else:
        return x*temp

print(power(2,2))


