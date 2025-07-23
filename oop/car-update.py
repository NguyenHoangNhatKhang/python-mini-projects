class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model  
    @property 
    def fullname(self):
        return f"{self.brand} {self.model}"
    
    @fullname.setter 
    def fullname(self,full_name):
        brand, model = full_name.split(" ")
        self.brand = brand
        self.model = model
    @fullname.deleter
    def fullname(self):
        self.brand = None
        self.model = None 
car = Car("Vinfast","Luxa2.0")
print(car.fullname)
print(car.brand)
del car.fullname
print(car.fullname)
print(car.brand)