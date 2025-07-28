class Node:
    def __init__(self,value,next=None):
        self.value = value 
        self.next = next


class Linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 


    def print_list(self):
        temp  = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node 
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node 
        self.length +=1 
        return True 
    
    def pop(self):
        if self.length == 0:
            return None 
        temp = self.head 
        pre = self.head 
        while(temp.next):
            pre = temp 
            temp = temp.next 
        self.tail = pre 
        self.tail.next = None 
        self.length -=1 
        if self.length == 0:
            self.head = None 
            self.tail = None 
        return temp     
        

my_list = Linkedlist(25)
my_list.append(20)
my_list.pop()
my_list.print_list()