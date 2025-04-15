# def firstn(n):
#     if n==0:
#         return
#     firstn(n-1)
#     print(n)
#
# firstn(3)

# def sumofdigits(n):
#     if n<10:
#         return n
#
#
#     return sumofdigits(n//10)+n%10
#
# print(sumofdigits(123))

def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1

    return fibo(n-1)+fibo(n-2)

print(fibo(6))