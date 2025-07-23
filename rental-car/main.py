from veh_class import Vehicle,Car,MotorBike,Bike 
from veh_data import vehicles
need_vehicle = True
while need_vehicle:
    vehicle_type = input("Whats the type of the vehicle you want to rent?: ").strip().lower()
    if vehicle_type == "car":
        for vehicle in vehicles:
            if vehicle_type == vehicle.type.lower():   
                vehicle.display()
    
    elif vehicle_type == "bike":
        for vehicle in vehicles:
            if vehicle_type == vehicle.type.lower():
                vehicle.display()
    

    elif vehicle_type == "motorbike":
        for vehicle in vehicles:
            if vehicle_type == vehicle.type.lower():
                vehicle.display()

    
    else:
        print(f"{vehicle_type} is not found!!!")
