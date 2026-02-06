class Bank:

    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello",cname,"Your Account Number Is",acno,"Is Opened With",balance,"Rs.")

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("sorry")
    def checkbalance(self):
        print("your balance is",self.balance)

b1=Bank()
b1.openAccount(40486506219,"Jay",40000)

while True:
    print("*"*40)
    print("1. deposit :")
    print("2. withdraw :")
    print("3. check balance :")
    print("4. exit")
    print("*"*40)
    choice=int(input("Enter Your Choice:"))
    print("*"*40)
    if choice==1:
        amount=int(input("enter deposit amount:"))
        b1.deposit(amount)
    elif choice==2:
        amount=int(input("enter withdrawl amount:"))
        b1.withdraw(amount)
    elif choice==3:
        b1.checkbalance()
    elif choice==4:
        print("thank you")
        print("*"*40)
        break
    else:
        print("invalid")
        print("*"*40)

        
