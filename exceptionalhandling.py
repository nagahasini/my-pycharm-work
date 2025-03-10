# n=int(input("enter num"))
#
# print(f"multiplication of{n}")
# try:
#  for i in range(1,11):
#     print(f"{n}x{i}={n*i}")
# except Exception as e:
# #     print(e)
#
#
#
# # try:
# #     a = int(input("numbers entry"))
# #     print(a)
# # except ValueError:
# #     print("enter integers")
#
# #lambda
# square = lambda z: z * 2  # Fixed the typo
# print(square(2))  # Correct call, outputs 4
#
# def fun(a, b):
#     return a(b)  # Call 'a' as a function, since it's a lambda function
#
# print(fun(lambda x: x + 2, 4))  # Outputs 6, lambda adds 2 to 4

# def fun(funcs,value):
#     return funcs(value)
# print(fun(lambda x:x+2,4))

###for list of functions
# l=[lambda x:x+2,lambda x:x*2,lambda x:x*x*x]
# def funcs(fun_2,value):
#     for i in fun_2:
#         value=i(value)
#     return value
#
# a=funcs(l,2)
# print(a)
# l=[1,2,3]
# newl= list((i*i for i in l))
# print(newl)

# ########MAP####
# # def cube(x):
#     return x*x*x
l=[1,2,3,4]
# newl=list(map(cube,l))
# print(newl)
# ###FILTER
def funcc(x):
    return x>3

o=list(filter(funcc,l))
print(o)