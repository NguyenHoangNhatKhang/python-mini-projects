height = float(input("Height: "))
weight = int(input("Weight: "))

bmi = weight / height**2

if height > 3 : 
    raise ValueError("Human height should not be over 3 meters.")
