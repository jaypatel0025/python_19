from abc import ABC,abstractmethod

class RBI(ABC):
    def show(self):
        print("Hello From RBI!")

    @abstractmethod
    def roi(self,r):
        pass

class SBI(RBI):
    def show(self):
        super().show()
        print("Hello From SBI!")
    def roi(self,r):
        print("Rate Of Intrest By SBI :",r)
        print("*"*40)

class HDFC(RBI):
    def show(self):
        super().show()
        print("Hello From HDFC!")
    def roi(self,r):
        print("Rate Of Intrest By HDFC :",r)
        print("*"*40)

class IDFC(RBI):
    def show(self):
        super().show()
        print("Hello From IDFC!")
    def roi(self,r):
        print("Rate Of Intrest By IDFC :",r)
        print("*"*40)

class BOB(RBI):
    def show(self):
        super().show()
        print("Hello From BOB!")
    def roi(self,r):
        print("Rate Of Intrest By BOB :",r)
        print("*"*40)

s1=SBI()
s1.show()
s1.roi(6.5)

h1=HDFC()
h1.show()
h1.roi(7)

i1=IDFC()
i1.show()
i1.roi(7.5)

b1=BOB()
b1.show()
b1.roi(8)
    
