### Errors and Exceptions 
# SyntaxError: This error occurs when the code is not written in the correct syntax. It can be caused by missing parentheses, incorrect indentation, or other syntax errors.
# RuntimeError: This error occurs when an error is detected during execution. It can be caused by various issues such as division by zero, file not found, or other runtime errors.
# LookupError: This error occurs when a variable or function is not found in the current scope. It can be caused by misspelling the variable name or trying to access a variable that has not been defined.
# OSError: This error occurs when an operating system-related error occurs. It can be caused by issues such as file not found, permission denied, or other OS-related errors.
# NameError: This error occurs when a variable or function is not defined. It can be caused by misspelling the variable name or trying to use a variable before it has been defined.
# TypeError: This error occurs when an operation is performed on a variable of the wrong type. It can be caused by trying to perform mathematical operations on a string or trying to concatenate a string with an integer.
# ValueError: This error occurs when a function receives an argument of the correct type but an inappropriate value. It can be caused by trying to convert a string to an integer that does not represent a valid number.
# IndexError: This error occurs when trying to access an index that is out of range in a list or other sequence. It can be caused by trying to access an index that does not exist in the list.
# KeyError: This error occurs when trying to access a key that does not exist in a dictionary. It can be caused by misspelling the key name or trying to access a key that has not been defined in the dictionary.
# AttributeError: This error occurs when trying to access an attribute that does not exist in an object. It can be caused by misspelling the attribute name or trying to access an attribute that has not been defined in the object.
# Importing necessary libraries

import sys
import traceback
import time
import logging

from user_exceptions import MyException


def logging_exception(filemode="a", message="This is a warning message"):
    logging.basicConfig(filename="app.log", filemode=filemode, format="Timestamp: %(asctime)s - Name: %(name)s - Level: %(levelname)s - Message: %(message)s")
    logging.warning(message)

def get_exception_info():
    try:  
        # Getting the exception information
        exception_type, exception_value, exception_traceback = sys.exc_info()
        # Extracting the file name, line number, procedure name, and line code from the traceback
        file_name, line_number, procedure_name, line_code = traceback.extract_tb(exception_traceback)[-1]

        exception_info = ''.join('[Time stamp]: ' + str(time.strftime('%d-%m-%Y %I:%M:%S %p')) + ' '
                                + '[File Name]: ' + str(file_name) + ' '
                                + '[Procedure Name]: ' + str(procedure_name) + ' '
                                + '[Error Message]: ' + str(exception_value) + ' '
                                + '[Error Type]: ' +str(exception_type) + ' '
                                + '[Line Number]: ' + str(line_number) + ' '
                                + '[Line Code]: ' + str(line_code))
        logging_exception(message=exception_info)
    except:
        pass
    return exception_info

def division_by_zero():
    try:
        division_by_zero = 1/1
    except:
        print(get_exception_info())
    else:
        print("Division successful")
    finally:
        pass
    
def main():
    # division_by_zero() # function to demonstrate division by zero error

    # raise exception: This statement is used to raise an exception intentionally. It can be used to signal an error condition or to indicate that a certain condition has been met. The exception can be raised with a specific message or with a custom exception class.
    # code: raise Exception("This is an exception message")

    # 4.3 User-defined Exceptions
    programming_language = ["JavaScript", "R", "Ruby", "PHP", "Java", "C#", "C", "C++", "Julia", "Go", "Python", "Perl"]
    for item in programming_language:
        if item != "Python":
            raise MyException(item, "My exception was raised with exception argument: {}".format(item))


if __name__ == '__main__':
    main()
