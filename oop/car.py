class  Car():
    tax = 1 
    car_number = 0
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model 
        self.price = price
        self.car_number +=1
    def Brand(self): #dùng để gắn logic 
        return self.brand
    def get_price(self):
        return self.price * self.tax
        # return self.price * Car.tax
    @classmethod 
    def set_tax(cls):
        cls.tax = 1.5
    
    @classmethod 
    def from_string(cls,car_string):
        brand,model,price = car_string.split('-')
        price = int(price)
        return cls(brand,model,price)
    @staticmethod 
    def check_price(price):
        if price <= 1000:
            return "this car is cheap"
        else:
            return "this car is expensivs"
        

car_1 = Car("Âudi","lussi",3000)
print(car_1.check_price(car_1.price))
