def oddeven(a):
    if a%2==0:
        print(a,"Is Even.")
    else:
        print(a,"Is Odd.")
def maxof2(a,b):
    if a>b:
        print(a,"Is Max.")
    else:
        print(b,"Is Max.")
def maxof3(a,b,c):
    if a>b:
        if a>c:
            print(a,"Is Max.")
        else:
            print(c,"Is Max.")
    elif b>c:
        print(b,"Is Max.")
    else:
        print(c,"Is Max.")
def prime(a):
    if a%2!=0:
        for i in range(3,int(a/2+1)):
            if a%i==0:
                print(a,"Is Not Prime.")
                break
        else:
            print(a,"Is Prime.")
    else:
        print(a,"Is Not Prime.")
