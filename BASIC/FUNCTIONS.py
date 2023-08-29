def fac(n):
    if n==1:
        return 1
    else:
   
        k=n*fac(n-1)
        return (k)

def forloop(n):
    f=1
    for i in range(1,n+1,1):
        f=f*i
    print(f)


m=int(fac(n=int(input())))
print(m)
forloop(int(input()))
