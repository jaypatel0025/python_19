import UDF

while True:
    print("*"*40)
    print("1. OddEven")
    print("2. Max of 2")
    print("3. Max of 3")
    print("4. Prime")
    print("5. Exit")
    print("*"*40)
    choice=int(input("Enter Choice:"))
    print("*"*40)
    if choice==1:
        n1=int(input("Enter Value :"))
        UDF.oddeven(n1)
        print("*"*40)
    elif choice==2:
        n1=int(input("Enter Value :"))
        n2=int(input("Enter Value :"))
        UDF.maxof2(n1,n2)
        print("*"*40)
    elif choice==3:
        n1=int(input("Enter Value :"))
        n2=int(input("Enter Value :"))
        n3=int(input("Enter Value :"))
        UDF.maxof3(n1,n2,n3)
        print("*"*40)
    elif choice==4:
        n1=int(input("Enter Value :"))
        UDF.prime(n1)
        print("*"*40)
    elif choice==5:
        print("Thank You.")
        break
    else:
        print("Invalid.")
        
