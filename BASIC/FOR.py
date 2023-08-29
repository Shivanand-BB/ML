def sumof(E):
 sum=0
 x=2*(E+1)
 for i in range(2,x,2):
  print(i)
  sum+=i
  L.append(sum)
  L.append(i)
 print("SUM OF",E,"EVEN NUMBERS IS\n",sum)
 print(L[0:2*(E+1)])
 
#SUM OF N NUMBERS
sum=0
L1=[sum]
L=[sum]
n=int(input("ENTER THE NUMBER\n"))
for i in range(1,n+1,1):
 print(i)
 sum+=i
print("SUM OF",n,"NUMBERS IS\n",sum)
L1.append(sum)
#SUM OF N EVEN NUMBERS
E=int(input("ENTER THE NUMBER\n"))
sumof(E)
