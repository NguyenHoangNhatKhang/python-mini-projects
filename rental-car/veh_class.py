class Vehicle:
    def __init__(self,brand,model,type):
        self.brand = brand 
        self.model = model 
        self.base_price = 100000
        self.type = type

    def display(self):
        print(f"""
=========================
🚗 Vehicle Information 🚗
-------------------------
Vehicle's type: {self.type} 
Brand: {self.brand} 
Model: {self.model}
Renting Price: {self.get_price():,}円
==========================
""")
    
    def __str__(self):
        return f"{self.type}"
    
    def __repr__(self):
        return self.__str__()
class Car(Vehicle):
    car_tax = 100000
    def __init__(self,brand,model,type="Car"):
        super().__init__(brand,model,type)
 
    def get_price(self):
        return self.base_price + self.car_tax
class Motorbike(Vehicle):
    motorbike_tax = 60000
    def __init__(self, brand, model,type="Motorbike"):
        super().__init__(brand, model,type)
       
    
    
    def get_price(self):
        return self.base_price + self.motorbike_tax
class Bike(Vehicle):
    bike_tax = 20000
    def __init__(self, brand, model,type="Bike"):
        super().__init__(brand, model,type)
        
    
    
    def get_price(self):
        return self.base_price + self.bike_tax

