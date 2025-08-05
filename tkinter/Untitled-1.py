def add(*args):
    sum = 0
    for n in args:
       sum += n
    return sum
          
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)


calculate(2, add=3,multiply=5)

class Car:
    def __init__(self,**kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
    
    def __str__(self):
     return f"make {self.make} model {self.model} {self.color} {self.seats}"

my_car = Car(make ="nissan",model="asaa",seats=6)
print(my_car)