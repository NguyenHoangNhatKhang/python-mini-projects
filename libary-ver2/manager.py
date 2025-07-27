from customer import Customer 
from libary import Library 
from book import Book
class Manager:
    customer = []
    def __init__(self):

        pass
    
    @classmethod
    def add_cus(cls,cus):
        return cls.customer.append(cus)
    
    @classmethod 
    def get_all(cls):
        if not cls.customer:
            return f"Customer list is empty"
        cus = ""
        for i,b in enumerate(cls.customer,start=1):
            cus += f"""
{i}.
name: {b.name}
id: {b.id}"""
        return cus 

