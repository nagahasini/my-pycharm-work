def union_usingsets(s1,s2):
    union=(s1.union(s2))
    return union

a= set(map(int,input("enter set one with commas").split(',')))
b= set(map(int,input("enter second set nums").split(',')))

r=union_usingsets(a,b)
print(r)