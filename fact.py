def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)

print(fact(5))


#011235
def fibo(num):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,num):
      c=a+b
      a = b
      b=c
      print(c)
fibo(4)
