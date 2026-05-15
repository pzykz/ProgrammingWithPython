### Working with Python
# # 5.1 Virtual Environments
# # A virtual environment is a self-contained directory that contains all the necessary files and dependencies for a specific Python project. It allows you to isolate the dependencies of different projects and avoid conflicts between them. You can create a virtual environment using the `venv` module in Python.
# # To create a virtual environment, you can use the following command in your terminal:
# python -m venv <Path>myenv
# # This will create a new virtual environment named `myenv` in the current directory. You can activate the virtual environment using the following command:
# # On Windows:
# <Path>myenv\Scripts\activate.bat

import unittest
import sys
import pandas as pd
import numpy as np
import scipy
import sklearn
import matplotlib
import seaborn
import statsmodels


# def main():
#     print("python: {}".format(sys.version))
#     print("numpy: {}".format(np.__version__))
#     print("pandas: {}".format(pd.__version__))
#     print("scipy: {}".format(scipy.__version__))
#     print("scikit-learn: {}".format(sklearn.__version__))
#     print("matplotlib: {}".format(matplotlib.__version__))
#     print("seaborn: {}".format(seaborn.__version__))
#     print("statsmodels: {}".format(statsmodels.__version__))

# if __name__ == '__main__':
#     main()

# Unit and Integrationtesting
# common used methods in unit testing:
# assertEqual(a, b) - checks if a and b are equal
# assertNotEqual(a, b) - checks if a and b are not equal
# assertTrue(x) - checks if x is True
# assertFalse(x) - checks if x is False
# assertIs(a, b) - checks if a and b are the same object
# assertIsNot(a, b) - checks if a and b are not the same object
# assertIsNone(x) - checks if x is None
# assertIsNotNone(x) - checks if x is not None
# assertIn(a, b) - checks if a is in b
# assertNotIn(a, b) - checks if a is not in b
# assertIsInstance(a, b) - checks if a is an instance of b
# assertNotIsInstance(a, b) - checks if a is not an instance of b

class MathOperations(object):
    def math_addition(self, number_1, number_2):
        '''
        provide math addition
        number_1: first number
        number_2: second number
        return: addition of first and second numbers
        '''
        result = number_1 + number_2
        return result

    def math_subtraction(self, number_1, number_2):
        '''
        provide math subtraction
        number_1: first number
        number_2: second number
        return: subtraction of first minus second numbers
        '''
        result = number_1 - number_2
        return result

class UnitTestMathOperations(unittest.TestCase):
    def test_addition(self):
        '''
        test math addition
        '''
        math_operations = MathOperations()
        result = math_operations.math_addition(2, 2)
        self.assertEqual(result, 4, "The addition should be 4")
    def test_subtraction(self):
        '''
        test math subtraction
        '''
        math_operations = MathOperations()
        result = math_operations.math_subtraction(2, 2)
        self.assertEqual(result, 0, "The subtraction should be 0")


if __name__ == "__main__":
    unittest.main()
