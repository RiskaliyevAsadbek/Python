# Object-Oriented Programming (OOP) Exercises
# 1. Circle Class
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area_calculator(self):
        import math
        return f'the are of circle is {self.radius **2 * math.pi}'
    def Circumference_calculator(self):
        import math
        return f' the Circumference of the circle is {2 * self.radius * math.pi}'
    
rad1 = Circle(9)
print(rad1.area_calculator())    
print(rad1.Circumference_calculator())

# 2. Person Class
# Write a Python program to create a Person class.
#  Include attributes like name, country, and date of birth. Implement a method to determine the person's age.
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def age_calculator(self, current_year):
        return f'you are {current_year - self.date_of_birth} years old'
    

person1 = Person('Edward', 'USA', 1986)
print(person1.age_calculator(2025))

# 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2
    def addition(self):
        return f'{self.num1} + {self.num2} = {self.num1 + self.num2}'
    def substraction(self):
        return f'{self.num1} - {self.num2} = {self.num1 - self.num2}'
    def multiply(self):
        return f'{self.num1} * {self.num2} = {self.num1 * self.num2}'
    def division(self):
        return f'{self.num1} / {self.num2} = {self.num1 / self.num2}'

numbers = Calculator(98, 5)
print(numbers.multiply())
print(numbers.division())
print(numbers.addition())
print(numbers.substraction()) 

# 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. 
# Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter()")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area_circle(self):
        pi_value = 3.14
        return f'Area -> Circle = {pi_value * self.radius ** 2}'
    def circumfereance_circle(self):
        pi_value = 3.14
        return f'Circumference -> Circle = {2 * pi_value * self.radius}'
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area_square(self):
        return f'Area -> Square = {self.side ** 2}'
    def perimeter_square(self):
        return f'Perimeter -> Square = {4 * self.side}'

class Triangle(Shape):
    def __init__(self,first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
    def perimeter_triangle(self):
        return f'Perimeter -> Triangle = {self.first_side + self.second_side + self.third_side}'
    def area_triangle(self):
        semi_perimeter = (self.first_side + self.second_side + self.third_side) / 2
        area = (semi_perimeter *(semi_perimeter - self.first_side)*(semi_perimeter-self.second_side)*(semi_perimeter-self.third_side)) ** 0.5
        return f'Area -> Triangle = {area}'
    
circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)
print(circle.area_circle())
print(square.area_square())
print(triangle.area_triangle()) 

# 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree.
# Include methods for inserting and searching for elements in the binary tree.
class Node:
    def __init__(self, value):
        self.value = value      
        self.left = None        
        self.right = None      
class BinarySearchTree:
    def __init__(self):
        self.root = None      

   
    def insert(self, value):
        new_node = Node(value)  
        if self.root is None:  
            self.root = new_node 
            return

       
        current = self.root
        while True:
            if value < current.value:          
                if current.left is None:     
                    current.left = new_node    
                    break
                current = current.left        
            elif value > current.value:        
                if current.right is None:      
                    current.right = new_node   
                    break
                current = current.right       
            else:
                
                break

    
    def search(self, value):
        current = self.root                    
        while current:                        
            if value == current.value:       
                return True              
            elif value < current.value:      
                current = current.left
            else:                             
                current = current.right
        return False                          


bst = BinarySearchTree()
bst.insert(15)
bst.insert(10)
bst.insert(20)
print(bst.search(15))
print(bst.search(30))


# 6. Stack Data Structure
# Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return f"Item {item} pushed!"

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty!"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
stack = Stack()
print(stack.push(10))
print(stack.push(20))
print(stack.pop())    

# 7. Linked List Data Structure
# Write a Python program to create a class representing a linked list data structure. 
# Include methods for displaying linked list data, inserting, and deleting nodes.
# Node class to represent each element in the Linked List
class Node:
    def __init__(self, data):
        self.data = data      # stores the data
        self.next = None      # pointer to the next node


class LinkedList:
    def __init__(self):
        self.head = None      

    def display(self):
        if self.head is None:
            print("The linked list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:   
            self.head = new_node
            return
        current = self.head
        while current.next:    
            current = current.next
        current.next = new_node

    def delete(self, key):
        current = self.head

        if current is None:
            print("The list is empty.")
            return

        if current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with data '{key}' not found.")
            return

        prev.next = current.next


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()

ll.delete(20)
ll.display()

ll.delete(40)  








# 8. Shopping Cart Class
# Write a Python program to create a class representing a shopping cart.
# Include methods for adding and removing items, and calculating the total price.
class ShoppingCart:
    def __init__(self):
        self.items = {}
    def add_item(self, item, price):
        self.items[item] = price
        print(f"{item} added to the cart at ${price}")
    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f"{item} removed from the cart")
        else:
            print(f"{item} not found in the cart")
    def calculate_total(self):
        total = sum(self.items.values())
        return total


cart = ShoppingCart()

cart.add_item("Apple", 2.5)
cart.add_item("Milk", 1.2)
cart.add_item("Bread", 1.8)

cart.remove_item("Milk")

print("Total price:", cart.calculate_total())

# 9. Stack with Display
# Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing, popping, and displaying elements.
class Stack:
    def __init__(self):
        self.list = []
    def push(self, item):
        self.list.append(item)
        print(f"{item} pushed onto stack")
    def pop(self):
        if len(self.list) != 0:
            removed = self.list.pop()
            print(f"{removed} popped from stack")
            return removed
        else:
            print(f'there is no element to pop')
    def display(self):
        if len(self.list) != 0:
            print(f'stack elements: {self.list}')
        else:
            print(f'stack is empty')

s = Stack()
s.push(10)
s.push(25)
s.push(54)
s.push(98)
s.display()
s.pop()
s.display()

# 10. Queue Data Structure
# Write a Python program to create a class representing a queue data structure. 
# Include methods for enqueueing and dequeueing elements.
class Queue:
    def __init__(self):
        self.queue = []
    def enqueueing(self, queue):
        self.queue.append(queue)
        print(f'{queue} is added to the queue')
    def dequeueing(self):
        if len(self.queue) != 0:
            dequeued = self.queue.pop(0)
            print(f'{dequeued} is dequeued from the queue')
            return dequeued
        else:
            print(f'the queue is already empty')
    def display(self):
        if len(self.queue) != 0:
            print(f'queue elements: {self.queue}')
        else:
            print('queue has no elements')

q = Queue()
q.enqueueing(67)
q.enqueueing(98)
q.enqueueing(54)
q.enqueueing(34)
q.display()
q.dequeueing()
q.display()

# 11. Bank Class
# Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.
class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self, account_number, initial_balance = 0):
        if account_number  in self.accounts:
            print(f'{account_number} is already exists')
        else:
            self.accounts[account_number] = initial_balance
            print(f'account {account_number} is created with the balance {initial_balance}')
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
             self.accounts[account_number] += amount
             print(f'deposited {amount} into account {account_number}')
        else:
            print('account is not found')
    def withdraw(self, account_number, amount):
        if self.accounts[account_number] >= amount:
            self.accounts[account_number] -= amount
            print(f'withdraw {amount} from account {account_number}')
        else:
            print('insufficient balance') 
    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f'balance for account {account_number} : {self.accounts[account_number]}')
        else:
            print('account not found')               

bank = Bank()
bank.create_account(1000, 1000)
bank.create_account(1001, 1998)
bank.create_account(1002, 9000)
bank.deposit(1000, 200)
bank.deposit(1002, 450)
bank.withdraw(1002, 5000)
bank.check_balance(1000)
bank.check_balance(1001)
bank.check_balance(1002)









             






    
    







            





        
    

         



                


          
    
              
        


       


            
        
