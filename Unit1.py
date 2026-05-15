### 1.1 data structures and string manipulation

# primitive data types
aInt = 10
aFloat = 3.14
aString = "Hello, World!"
aBoolean = True
print("aInt:", aInt)
print("aFloat:", aFloat)
print("aString:", aString)
print("aBoolean:", aBoolean)

# non-primitive data types
aList = [1, 2, 3, 4, 5]
aTuple = (1, 2, 3, 4, 5)
aDictionary = {"key1": "value1", "key2": "value2"}
aSet = {1, 2, 3, 4, 5}
aFrozenSet = frozenset([1, 2, 3, 4, 5])
print("aList:", aList)
print("aTuple:", aTuple)
print("aDictionary:", aDictionary)
print("aSet:", aSet)
print("aFrozenSet:", aFrozenSet)

# # string manipulation
# # string length using len() method
string_0 = "Python is becoming the worlds most popular programming language today"
# print("Length of string_0:", len(string_0))
# # string concatenation using + sign
# string_0 = "Python is becoming the worlds most " + "popular programming language today"
# # print(string_0)
# # string concatenation using join() method
# string_2 = "".join(("Python is becoming the worlds most ", "popular programming language today"))
# print(string_2)
# # substrings (or splices) using [start, start + length]; get 'Python' word from the start
# string_3 = string_0[0:6]
# print(string_3)
# # remove 'Python' word from the start, skips first 7 characters
# string_4 = string_0[7:]
# print(string_4)
# # remove 'today' word from the end
# string_5 = string_0[:-6]
# print(string_5)
# # select 'programming' word only
# string_6 = string_0[43:54]
# print(string_6)
# # count how many times letter 'a' is in string
# string_7 = string_0.count("a")
# print(string_7)
# # find what position 'language' word start
# string_8 = string_0.find("language")
# print(string_8)
# # remove any whitespace from the start to end
# string_9 = string_0.strip()
# print(string_9)
# # convert to lower case
# string_10 = string_0.lower()
# print(string_10)
# # convert to upper case
# string_11 = string_0.upper()
# print(string_11)
# # replace 'Python' word with 'Java'
# string_12 = string_0.replace("Python", "Java")
# print(string_12)
# # split string into substring in 'most' word
# string_13 = string_0.split("most")
# print(string_13)
# # check if 'popular' word is in string
# string_14 = "popular" in string_0
# print(string_14)
# # check if 'POPULAR' word is in string
# string_15 = "POPULAR" not in string_0
# print(string_15)

### 1.2 functions

def print_message(message):
    print("The message is: {}".format(message))

def main():
    my_message = string_0
    print_message(my_message)

if __name__ == "__main__":
    main()


def addition_two_number(number_1, number_2):
    """
    docstring: this function takes two numbers as input and returns their addition
    """
    number_addition = number_1 + number_2
    return (number_addition)

result = addition_two_number(aInt, aFloat)
print("The addition of {} and {} is: {}".format(aInt, aFloat, result))


def payment_day(working_hours, payment_hour=None):
    '''
    docstring: this function takes working hours and payment per hour as input and returns total payment for the day. If payment per hour is not provided, it defaults to 25.
    '''
    if payment_hour is None:
        payment_hour = 25
    total_payment = working_hours * payment_hour
    return total_payment

working_hours = 8
total_payment = payment_day(working_hours)
print("Total payment for the day is: {}".format(total_payment))


# *args and **kwargs are used to pass a variable number of arguments to a function. *args is used to pass a variable number of non-keyword arguments, while **kwargs is used to pass a variable number of keyword arguments.

def sum_number(*args):
    total_sum = sum(args)
    return total_sum

def args_test():
    result_1 = sum_number(*aList)
    print("result_1: {}".format(result_1))
    result_2 = sum_number(*aSet)
    print("result_2: {}".format(result_2))

def kwargs_test(**kwargs):
    for key, value in kwargs.items():
        print("The value of {}: {}".format(key, value))

args_test()

kwargs_test(**aDictionary)   

# scope of variables
def outer_function():
    outer_variable = "I am an outer variable"
    print(outer_variable)

    def inner_function():
        inner_variable = "I am an inner variable"
        print(inner_variable)
        print(outer_variable)

    inner_function()
    # print(inner_variable) # this will raise an error because inner_variable is not in the scope of outer_function


x_global = 100
def calculate_double(x):
    global x_local
    x_local = x * 2
    return x_local

def scope_test():
    value = 10
    value_double = calculate_double(value)
    print("The value double in scope_test() is: {}".format(value_double))
    
scope_test()
print("The x_global in scope_test() is: {}".format(x_global))

# nested functions and closures: a nested function is a function defined inside another function. A closure is a nested function that has access to the variables of the outer function even after the outer function has finished executing.
def outer_function_closure(x):
    def inner_function_closure():
        return x * 2
    return inner_function_closure
closure_function = outer_function_closure(10)
result_closure = closure_function()
print("The result of closure function is: {}".format(result_closure))

# lambda functions: a lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. It is often used for short, simple functions that are not worth defining with a full function definition.
lambda_function = lambda x: x * 2
result_lambda = lambda_function(10)
print("The result of lambda function is: {}".format(result_lambda))


### 1.3 Flow Control
# If-elif-else 
from zipfile import Path

import numpy as np

def check_number(num):
    global num_global
    num_global = num
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    
print("The result for check_number is: {}".format(check_number(np.random.randint(-10, 10))))
print("The number used for check_number was: {}".format(num_global))

# for loop
# for i in range(5):
#     print("The for-loop value of i is: {}".format(i))

# while loop + break + continue statement
i = 0
while i < 5:
    i += 1
    if i == 4:
        break
    elif i == 3:
        print("The while-loop value of i was: {}".format(i)+", and the loop will be skipped due to pass statement")
        pass
    else:
        print("The while-loop value of i is: {}".format(i))
        continue


# 1.4 input output and file handling
# input and output
# user_input = input("Please enter a number: ")
# print("You entered: {}".format(user_input))
def write_file(string="unnamed title"):
    file_test = open("{}.txt".format(string), "w")
    file_test.write("Python is a great language.\nSure!\n")
    file_test.close()

def add_line_to_file(title="unnamed title", line=""):
    file_test = open("{}.txt".format(title), "a")
    file_test.write(line + "\n")
    file_test.close()

def read_file(title="unnamed title"):
    file_test = open("{}.txt".format(title), "r")
    content = file_test.read()
    file_test.close()
    return content

def read_file_line_by_line(title="unnamed title"):
    file_test = open("{}.txt".format(title), "r")
    for line in file_test:
        print(line.strip())
    file_test.close()

write_file("named title")
add_line_to_file("named title", "Add this new line to the end of the file")
add_line_to_file("named title", "Add this another line to the end of the file")
add_line_to_file("named title", "And for the last time, add this line to the end of the file")
# print(read_file("named title"))
print(read_file_line_by_line("named title"))

#creating a path and reading/writing files in a specific path
# def read_file_in_path():
#     folder_path = Path(r"C:/Users/nikol/Documents/Bildung/LFH Leibniz-FH/Module/6.SEM Verteilte Systeme/")
#     file_name = "vs.txt"
#     file_path_name = folder_path / file_name
#     file_test = open(file_path_name, "r")
#     for line in file_test:
#         print(line.strip())

# read_file_in_path()

# Logging
import logging
def logging_test(filemode="a", message="This is a warning message"):
    logging.basicConfig(filename="app.log", filemode=filemode, format="Timestamp: %(asctime)s - Name: %(name)s - Level: %(levelname)s - Message: %(message)s")
    logging.warning(message)

logging_test(filemode="a", message="This is just a test message for logging")