l1=[]
cubes=[]
even=[]
odd=[]

n=int(input("Enter Number:"))
for i in range(1,n+1):
    l1.append(i)
print("List:",l1)

cubes=list(map(lambda j:j*j*j,l1))
even=list(filter(lambda k:k%2==0,cubes))
odd=list(filter(lambda k:k%2!=0,cubes))

print("Cubes:",cubes)
print("Even Cubes:",even)
print("Odd Cubes:",odd)
