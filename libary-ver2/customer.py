import random
class Customer:
    def __init__(self,name):
        self.name = name
        self.num = random.randint(0,9999)
        self.char = random.choice([chr(i) for i in range(65,91)])
        self.id = f"{self.char}{self.num:03}"

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name 
    


    

  


    
    


