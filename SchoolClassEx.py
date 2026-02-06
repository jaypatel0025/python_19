class School:

    def studentdetails(self,sname,standard,rno,totalfees):
        self.sname=sname
        self.standard=standard
        self.rno=rno
        self.totalfees=totalfees
        self.paidfees=0
        print("hello",sname,"from standard",standard,"your roll no. is",rno)

    def pay_fees(self,amount):
        if self.paidfees!=self.totalfees:
            if self.paidfees+amount<=self.totalfees:
                self.paidfees=amount
                print("fees paid successfully.")
            else:
                print("your amount",amount,"is higher than fees.")
        else:
            print("you already paid full fees")
            
    def remaining_fees(self):
        remaining=self.totalfees-self.paidfees
        print("remaining fees:",remaining)

    def total_fees(self):
        print("your total fees is",self.totalfees)

s1=School()
s1.studentdetails("Jay","10th",25,5000)

while True:
    print("*"*40)
    print("1. total fees :")
    print("2. pay fees :")
    print("3. remaining fees :")
    print("4. exit")
    print("*"*40)
    choice=int(input("Enter Your Choice:"))
    print("*"*40)
    if choice==1:
        s1.total_fees()
    elif choice==2:
        amount=int(input("enter your paying amount:"))
        s1.pay_fees(amount)
    elif choice==3:
        s1.remaining_fees()
    elif choice==4:
        print("thank you")
        print("*"*40)
        break
    else:
        print("invalid")
        print("*"*40)
