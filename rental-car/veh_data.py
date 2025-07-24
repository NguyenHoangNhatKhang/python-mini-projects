from veh_class import Vehicle,Car,Motorbike,Bike 
from random import choice 
# vehicles = [
#     Car("Audi", "LX280"),
#     Car("Toyota", "Camry"),
#     Car("BMW", "320i"),
#     Car("Ferrari", "Roma"),
#     Car("Mercedes", "C300"),
    
#     MotorBike("Yamaha", "Exciter 150"),
#     MotorBike("Honda", "Winner X"),
#     MotorBike("Suzuki", "Raider"),
#     MotorBike("Kawasaki", "Z125"),
#     MotorBike("SYM", "Galaxy"),
    
#     Bike("Martin", "MTB-01"),
#     Bike("Asama", "CityBike"),
#     Bike("GIANT", "Escape 3"),
#     Bike("Trek", "FX 1"),
#     Bike("Thống Nhất", "Fixie")
# ]



car_brands = ["Audi", "Toyota", "BMW", "Ferrari", "Mercedes", "Honda", "Ford", "Chevrolet", "Hyundai", "Kia"]
car_models = ["LX280", "Camry", "320i", "Roma", "C300", "Civic", "Focus", "Malibu", "Sonata", "Sorento"]

motor_brands = ["Yamaha", "Honda", "Suzuki", "Kawasaki", "SYM", "Piaggio", "Ducati", "Harley", "BMW", "Aprilia"]
motor_models = ["Exciter 150", "Winner X", "Raider", "Z125", "Galaxy", "Liberty", "Monster", "Street 750", "G310R", "SR150"]

bike_brands = ["Martin", "Asama", "GIANT", "Trek", "Thống Nhất", "Merida", "Specialized", "Cannondale", "Btwin", "Phoenix"]
bike_models = ["MTB-01", "CityBike", "Escape 3", "FX 1", "Fixie", "Crossway", "Sirrus", "Quick 4", "Rockrider", "Classic"]


vehicles = []


def generate_veh(veh_type=input("What types of vehicle?:").strip().title(),quantity=int(input(f"How many vehicles would you like to see:"))):
    for i in range(quantity):
        if veh_type == "Car":
            car_brand = choice(car_brands)
            car_model = choice(car_models)
            vehicles.append(Car({car_brand},{car_model}))
        elif veh_type == "Motorbike":
            motor_brand = choice(motor_brands)
            motor_model = choice(motor_models)
            vehicles.append(Motorbike({motor_brand},{motor_model}))
        elif veh_type == "Bike":
            bike_brand = choice(bike_brands)
            bike_model = choice(bike_models)
            vehicles.append(Bike({bike_brand},{bike_model}))
        else: 
            print(f"Your {veh_type} of Vehicles are invalid!")
            break
generate_veh()