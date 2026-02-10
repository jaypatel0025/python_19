class car:
    wheels=4

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

car1=car("toyota","camary")
car2=car("honda","civic")


print(car1.wheels)
print(car2.wheels)
print(car1.brand)
print(car2.brand)
print(car1.model)
print(car2.model)
        
