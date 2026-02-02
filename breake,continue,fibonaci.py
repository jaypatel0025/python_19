#for i in range(1,10):
   # if i==5:
        #break
        #continue
   # print("i:",i)



a,b=0,1
n=int(input("enter n:"))
print(a,end=" ")

while b<n:
    print(b,end=" ")
    a,b=b,a+b
