def isarmstrong(n):
    original=n
    s = str(n)
    length = len(s)
    po = 0
    while n != 0:
        l = n % 10
        po = po + l ** length
        n = n // 10
    return po == original


print(isarmstrong(15))