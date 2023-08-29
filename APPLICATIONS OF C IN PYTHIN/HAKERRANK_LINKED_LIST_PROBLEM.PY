#123 487 ==== 784+321
l1=[]
l2=[]
l3=[]
l4=[]
k=0
l1.append(int(input("ENTER THE FIRST NUMBER\n")))
l2.append(int(input("ENTER THE SECOND NUMBER\n")))
m=l1[0]
i=0
k=0
while m!=0:
   temp=m%10
   l3.append(temp)
   m=m//10
   k+=1
ok=k-1
k=0
m=l2[0]
while m!=0:
   temp=m%10
   l4.append(temp)
   m=m//10
   k+=1
tk=k-1
s=0

while ok>=0:
   o=l3[ok]
   s=s+o*(10**i)
   i+=1
   ok-=1
print("REVERSED NUMBERS")
print(s)
s1=s
i=0
s=0
while tk>=0:
   o=l4[tk]
   s=s+o*(10**i)
   i+=1
   tk-=1
print(s)
print("SUM OF REVERSED NUMBERS\n")
print(s+s1)
m=s+s1
l5=[]
while m!=0:
   temp=m%10
   l5.append(temp)
   m=m//10
print(l5)

#optmized
