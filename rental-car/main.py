from veh_class import Vehicle,Car,Motorbike,Bike 
from veh_data import vehicles
need_vehicle = True
while need_vehicle:
    found = False
    vehicle_type = input("Whats the type of the vehicle you want to rent?: ").strip().lower()
    for vehicle in vehicles:
        if vehicle_type == vehicle.type.lower():
            vehicle.display()
            found = True 
    
    if not found: 
        print("== Available types: car / motorbike / bike ==")
        print(f"{vehicle_type} is not found!")
        
            