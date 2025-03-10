class Sorting:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def myfun(p):
    return p.x

l=[Sorting(1,5),Sorting(0,5)]
l.sort(key=myfun)
for i in l:
    print(i.x,i.y)

