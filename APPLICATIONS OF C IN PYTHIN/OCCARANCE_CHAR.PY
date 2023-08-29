#PRINTING THE OCCURANCE
def occur(l1,k):
 h=0
 for i in range(0,k,1):
  copy=l1[i]
  for j in range(0,k,1):
   if l1[j]==-999:
    continue
   elif l1[j]==copy:
    l1[j]=-999
    h+=1
  if copy!=-999:
   print(copy,"OCCURED",h,"TIMES")
  h=0
#CREATING A SUITABLE ARRAY
def find(l,n):
 temp=0
 k=0
 h=0
 l1=[]
 for i in range(0,n,1):
  m=l[i]
  while m!=0:
   temp=m%10
   l1.append(temp)
   m=m//10
   k+=1
 print(l1)
 occur(l1,k)

#MAIN FUNCTION
n=int(input("ENTER THE NUMBER OF ARRAY ELEMENTS\n"))
print("ENTER THE ELEMENTS\n")
l=[]
for i in range(0,n,1):
 l.append((input()))
print(l)
l=sorted(l)
print(l)
occur(l,n)