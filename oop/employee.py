class Employee:
    co_salary = 1.04
    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@gmail.com"
    
    def Get_email(self):
        return self.email 
    def apply_co_salary(self):
        self.pay = int(self.pay * self.co_salary)
        return self.pay 
    def __repr__(self):
        return f"Employee {self.first}, {self.last}, {self.pay}"
    
    def __str__(self):
        return f"{self.Get_email()}- {self.apply_co_salary()}"
    
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.Get_email())
class Developer(Employee):
    co_salary = 1.02
    def __init__(self,first,last,pay,pro_lang):
        super().__init__(first,last,pay)
        self.pro_lang = pro_lang

class Manager(Employee):
    co_salary = 4.00 
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees == None:
            self.employees =  []
        else: 
            self.employees = employees 
    # def add_employees(self,required_employess):
    #     self.required_employees = required_employess
    #     self.employees = self.employees + self.required_employees
    #     return self.employees 
    
    def add_employees(self,name_employees):
        #sai kh tối ưu 
        if name_employees not in self.employees:
            self.employees.append(name_employees)
            return self.employees
    def remove_employees(self,name_employees):
        if name_employees is None :
            return "not found"
        elif name_employees in self.employees:
            self.employees.remove(name_employees)
            return self.employees
        return f"not found in the list"
    def print_employees(self):
        for name_employees in self.employees:
            print(name_employees.Get_email())

class Secretary(Employee):
    def __init__(self, first, last, pay,job):
        super().__init__(first, last, pay)
        self.job = job 

dev1 = Developer("khang","nguyenhoangnhat",2000,"Python")
dev2 = Developer("Khoa","khoi",5555,"c++")
man = Manager("khoa","Phamthien",500,[dev1,dev2])
sec1 = Secretary("ngoc","hiue",60000,"eat with manager")
print(str(dev1))
print(repr(dev1))
print(dev1 + dev2)
print(dev1.__len__())