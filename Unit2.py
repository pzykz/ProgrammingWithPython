### 2.1 Scopes and namespaces
# Scopes are the regions of a program where a particular variable is accessible. There are four types of scopes in Python: local, enclosing, global, and built-in.

import iterator_call
from iterator_class import SequenceNumber
from ast import main


def scope_testing():
    def local_scope():
        spam = "local spam defined"

    def nonlocal_scope():
        nonlocal spam
        spam = "nonlocal spam defined"
        
    def global_scope():
        global spam
        spam = "global spam defined"
        
    spam = "testing the spam"
    local_scope()
    print("After local scope test:", spam)
    nonlocal_scope()
    print("After nonlocal scope test:", spam)
    global_scope()
    print("After global scope test:", spam)

scope_testing()
print("In global scope:", spam)


### 2.2 Classes and Inheritance
# A class is a blueprint for creating objects. It defines a set of attributes and methods that
# can be used to create instances of the class.
class TextBook:
    def __init__(self, book_title, pages_number):
        self.book_title = book_title
        if pages_number is not None:
            self.pages_number = pages_number
        else:
            self.pages_number = None

    def print_book_title(self, title):
        print("Book Title:", title)

    def print_book_pages_number(self,pages_number):
        if self.pages_number is not None:
            print("Number of Pages:", self.pages_number)


book_title = "Programming with Python"
pages_number = 300
# object text_book is the instant of the class TextBook():
text_book = TextBook(book_title, pages_number)
# calling print_book_title() method
text_book.print_book_title(book_title)
# calling print_book_pages_number method
text_book.print_book_pages_number(pages_number)


# Constructor is a special method that is called when an object is created. It is used to initialize the attributes of the object. In Python, the constructor method is defined as __init__().
class TextBookConstructor:
    def __init__(self, title, pages):
        '''Constructor method to initialize the title and pages attributes of the TextBookConstructor class.'''
        self.title = title
        self.pages = pages

    def print_book_info(self):
        '''Method to print the title and pages of the book.'''
        print("Book Title:", self.title)
        print("Number of Pages:", self.pages)
    

# Inheritance is a mechanism in which a new class is derived from an existing class. The new class is called the child class or subclass, and the existing class is called the parent class or superclass. The child class inherits the attributes and methods of the parent class, and can also have its own attributes and methods.
class PersonClass(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def print_name(self, person_type):
        print("The " + person_type + " name is: " + self.first_name + " " + self.last_name)

    def get_name_email(self, email):
        name_email = "The email of " + self.first_name + " " + self.last_name + " is: " + email
        return name_email

    def is_employee(self):
        return True
    
class EmployeeClass(PersonClass):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
    
    def print_employee_id(self, id):
        print("Employee " + self.first_name + " " + self.last_name + " id is: " + str(id))

    def is_employee(self):
        return True
    
class CustomerClass(PersonClass):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
    
    def print_customer_phone(self, customer_phone):
        print("Customer " + self.first_name + " " + self.last_name +
              " phone is: " + customer_phone)

    def is_employee(self):
        return False

def class_testing():
    # print employee name
    first_name = "John"
    last_name = "Smith"
    employee_class = EmployeeClass(first_name, last_name)
    person_type = "employee"
    employee_class.print_name(person_type)

    # print employee id
    employee_id = 100
    employee_class.print_employee_id(employee_id)
    
    # check if an employee is employee
    result = employee_class.is_employee()
    print("Employee: " + str(result))
    
    # print customer name
    first_name = "David"
    last_name = "Johnson"
    customer_class = CustomerClass(first_name, last_name)
    person_type = "customer"
    customer_class.print_name(person_type)
    
    # print customer phone number
    customer_phone = "+1.800.503.987.6543"
    customer_class.print_customer_phone(customer_phone)
    
    # check if a customer is employee
    result = customer_class.is_employee()
    print("Employee: " + str(result))

class_testing()

# 2.3 Iterators and generators
# An iterator is an object that can be iterated (looped) upon. It returns data one element at a time. In Python, an iterator is an object that implements the __iter__() and __next__() methods.
# def iterator_testing():
#     number_list = [1, 2, 3, 4, 5]
#     number_list_iter = iter(number_list)
#     # print 1
#     print(next(number_list_iter))
#     # print 2
#     print(next(number_list_iter))
#     # print 3
#     print(next(number_list_iter))
#     # print 4
#     print(next(number_list_iter))
#     # print 5
#     print(next(number_list_iter))
#     # # an error occurred - StopIteration
#     # print(next(number_list_iter))

# iterator_testing()

# iterator_call.iterator_call()

# Generators are a special type of iterators that are defined using a function. They use the yield statement to return data one element at a time. When a generator function is called, it returns a generator object that can be iterated upon.
def sequence_generator(low, high):
    while low < high:
        yield low
        low += 1

def generator_testing():
    number_list = []
    for number in sequence_generator(0, 5):
        number_list.append(number)
    print(number_list)

generator_testing()

# itertools
from itertools import count, cycle, repeat

def count_generator(start, step):
    for number in count(start, step):
        if number < 10:
            yield number
        else:
            break

def cycle_generator(iterable):
    person = cycle(iterable)
    count = 0
    while count != 6:  # Limit the number of iterations for demonstration
        print(next(person))
        count += 1

print(list(count_generator(0, 2)))
cycle_generator(['Person', 'Employee', 'Customer'])