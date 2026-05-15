# Standard python libraries
import config
import datetime
import numpy as np
import pandas as pd
import os
from scipy.special import jn, yn, jn_zeros, yn_zeros
from scipy.integrate import quad, dblquad, tplquad
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import random as randn
import sys
from pathlib import PureWindowsPath

def main():
    def np_exc_result():
        '''
        numpy library is for numerical computing, which provides support for large, multi-dimensional arrays and matrices, 
        along with a collection of mathematical functions to operate on these arrays.
        '''
        print("using numpy library for numerical computing:")

        # print the version of numpy library
        print("numpy version: {}".format(np.__version__))

        # create a numpy array from a list and a tuple, and print the array
        np_array = a = np.array([1, 2, 3, 4, 5])
        print("create array from a list: \n{}".format(np_array))

        # create a numpy array from a tuple and print the array
        np_array = a = np.array((6, 7, 8, 9, 10))
        print("create array from a tuple: \n{}".format(np_array))

        # print the shape of the array, which is a tuple of integers indicating the size of the array in each dimension
        np_shape = np_array.shape
        print("one-dimension array shape, 5 elements: {}".format(np_shape))

        # create a two-dimensions array from a list of lists and print the array
        np_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        print("two-dimensions array: \n{}".format(np_array))

        # print the shape of the two-dimensions array, which is a tuple of integers indicating the size of the array in each dimension
        np_shape = np_array.shape
        print("two-dimensions array shape, 2 rows and 5 columns: \n{}".format(np_shape))

        # reshape the one-dimension array to a two-dimensions array and print the reshaped array
        np_array = a = np.array((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
        np_reshape = np_array.reshape(5, 2)  # reshape array to 5 rows and 2 columns
        print("returns the array with a modified shape, 5 rows and 2 columns: \n{}".format(np_reshape))

        # print the number of dimensions, size, data type of the elements, the size in bytes of each element and the buffer containing the actual elements of the array
        np_dim = np_array.ndim  # number of dimensions of the array
        print("array dimensions: \n{}".format(np_dim))

        # size of the array, which is the total number of elements in the array, equal to the product of the shape dimensions
        np_size = np_array.size  # number of elements in the array
        print("array size: column number x row number: {}".format(np_size))
        
        # data type of the elements in the array, which is a numpy data type object that describes the type of the elements in the array, such as int32, float64, etc.
        np_dtype = np_array.dtype  # data type of the elements in the array
        print("data type of the elements in the array: \n{}".format(np_dtype))
        
        # the size in bytes of each element of the array, which is determined by the data type of the elements and can be accessed through the itemsize attribute of the array
        np_itemsize = np_array.itemsize  # the size in bytes of each element of the array
        print("the size in bytes of each element of the array: {}".format(np_itemsize))
        
        # the buffer containing the actual elements of the array, which is a memory view object that provides access to the underlying data of the array, and can be accessed through the data attribute of the array
        np_data = np_array.data  # the buffer containing the actual elements of the array, don't need it for calculations
        print("the buffer containing the actual elements of the array, don't need it for calculations: \n{}".format(np_data))
        print(np_data)

        array_1 = np.array([1, 2, 3, 4, 5])
        array_2 = np.array([6, 7, 8, 9, 10])
        
        array_result = array_1 + array_2
        print("addition operation:")
        print(array_result)
        
        array_result = array_1 - array_2
        print("subtraction operation:")
        print(array_result)
        
        array_result = array_2 - array_1
        print("subtraction operation:")
        print(array_result)
        
        array_result = array_1 * array_2
        print("multiplication operation:")
        print(array_result)
        
        array_result = array_1 / array_2
        print("division operation:")
        print(array_result)
        
        # calculate the pearson product-moment correlation coefficients between two arrays, which is a measure of the linear correlation between two variables, and can be calculated using the corrcoef function of numpy library
        np_corrcoef = np.corrcoef(array_1, array_2)  # pearson product-moment correlation coefficients
        print("pearson product-moment correlation coefficients: \n{}".format(np_corrcoef))
        
        # calculate the covariance between two arrays, which is a measure of the joint variability of two random variables, and can be calculated using the cov function of numpy library
        np_mean = np.mean(array_1)  # arithmetic mean of the array elements
        print("arithmetic mean: \n{}".format(np_mean))
        
        # calculate the weighted average of the array elements, which is a measure of central tendency that takes into account the relative importance of each element in the array, and can be calculated using the average function of numpy library with the weights parameter
        np_average = np.average(array_1)  # weighted average of the array elements
        print("weighted average:")
        print(np_average)
        
        # calculate the standard deviation of the array elements, which is a measure of the amount of variation or dispersion of a set of values, and can be calculated using the std function of numpy library
        np_std = np.std(array_1)  # standard deviation of the array elements
        print("standard deviation: \n{}".format(np_std))
        
        # calculate the median of the array elements, which is the middle value of a sorted list of numbers, and can be calculated using the median function of numpy library
        np_median = np.median(array_1)  # median of the array elements
        print("median: \n{}".format(np_median))
        
        # calculate the variance of the array elements, which is a measure of the spread of a set of values, and can be calculated using the var function of numpy library
        np_variance = np.var(array_1)  # variance of the array elements, the average of the squared deviations from the mean
        print("variance: \n{}".format(np_variance))
        
        # calculate the minimum and maximum of the array elements, which are the smallest and largest values in the array, respectively, and can be calculated using the min and max functions of numpy library
        np_min = np.min(array_1)  # minimum of the array elements
        print("minimum: \n{}".format(np_min))

        # calculate the maximum of the array elements, which is the largest value in the array, and can be calculated using the max function of numpy library
        np_max = np.max(array_1)  # maximum of the array elements
        print("maximum: \n{}".format(np_max))
        
        # calculate the sum of the array elements, which is the total of all the values in the array, and can be calculated using the sum function of numpy library
        np_summa = np.sum(array_1) # sum of the array elements
        print("summa: \n{}".format(np_summa))


    ### Pandas library
    def create_df():
        # create a dataframe from a dictionary
        dictionary = {"col 1": [1., 2., 3., 4., 5.], "col 2": [6, 7, 8, 9, 10],"col 3": ["uno", "dos", "tres", "cuatro", "cinco"]}
        df_data = pd.DataFrame(data=dictionary, index=["row1", "row2", "row3","row4", "row5"])
        print(df_data)


    def pd_exc_result():
        '''
        pandas library is for data manipulation and cleansing, which provides data structures and functions for working with structured data, 
        such as tabular data in the form of data frames, and offers powerful tools for data cleaning, transformation, and analysis.
        '''
        print("using pandas library for data manipulation and cleansing:")
        print()

        # get the path of the project directory
        project_directory_path = PureWindowsPath(os.path.dirname(sys.argv[0]))
        print("project directory path: {}".format(project_directory_path))
        print()

        # get the path of the input file
        input_file_path = os.path.join(project_directory_path, config.INPUT_FILE_PATH)
        print("input file path: {}".format(input_file_path))
        print()

        # get the path of the output file
        output_file_path = os.path.join(project_directory_path, config.OUTPUT_FILE_PATH)
        print("output file path: {}".format(output_file_path))
        print()

        # read the input file and create a pandas data frame
        df_input_file = pd.read_csv(filepath_or_buffer=input_file_path, sep=",", encoding="utf-8")
        print("pandas data frame for input file:")
        print(df_input_file)
        print()

        # print the number of rows and columns in the data frame
        print("number of rows and columns: {}".format(df_input_file.shape))
        print()

        # print the file information, including the data types of the columns and the number of non-null values in each column
        print("file information: {}".format(df_input_file.info()))
        print()

        # change str into object data type for column four and eight
        df_input_file["four"] = df_input_file["four"].astype("object")
        df_input_file["eight"] = df_input_file["eight"].astype("object")
        print("change str into object data type for column four and eight: \n{}".format(df_input_file.info()))
        print()

        # print the summary descriptive statistics for the numerical columns in the data frame
        print("summary descriptive stats for numerical columns: \n{}".format(df_input_file.describe()))
        print()
        
        # print the frequency distribution for the categorical column four in the data frame
        df_result = df_input_file["four"].value_counts()
        print("frequency distribution for categorical column four: \n{}".format(df_result))  
        print()
        
        # print the frequency distribution for the categorical column eight in the data frame
        df_result = df_input_file["eight"].value_counts()
        print("frequency distribution for categorical column eight: \n{}".format(df_result))  
        print()

        # print the number of missing values (nan) by columns in the data frame
        df_result = df_input_file.apply(lambda x: sum(x.isnull()), axis=0)
        print("missing values (nan) by columns: \n{}".format(df_result))
        print()
        
        # print the duplicated rows in the data frame
        df_result = df_input_file.duplicated()
        print("duplicated rows: \n{}".format(df_result))
        print()
        
        # drop the duplicated rows and keep the first occurrence in the data frame
        df_input_file = df_input_file.drop_duplicates(keep="first")
        print("drop duplicated rows and keep the first: \n{}".format(df_input_file))
        print(df_input_file)
        print()

        # replace nan values with the mean value in columns one and two
        df_input_file = df_input_file.fillna(df_input_file[["one","two"]].mean())
        print("replace nan values with the mean value in columns one and two: \n{}".format(df_input_file))
        print()

        # replace nan values with the median value in column three
        df_input_file["three"] = df_input_file["three"].fillna(df_input_file["three"].median())
        print("replace nan values with the median value in column three: \n{}".format(df_input_file))
        print()

        # replace nan values with the most frequent value in column four
        df_input_file["four"] = df_input_file["four"].fillna("club")
        print("replace nan values with the 'club' string in column four: \n{}".format(df_input_file))
        print()

        # replace nan values with the true boolean in column five
        df_input_file["five"] = df_input_file["five"].fillna(True)    
        print("replace nan values with the true boolean in column five: \n{}".format(df_input_file))
        print()

        # replace nan values with the current date in column six
        now = datetime.datetime.now().strftime("%m/%d/%Y")
        df_input_file["six"] = df_input_file["six"].fillna(str(now))
        df_input_file["six"] = pd.to_datetime(df_input_file["six"])
        print("replace nan values with the current date in column six: \n{}".format(df_input_file))
        print()
        
        # replace nan values with the £0.0 string in column seven
        df_input_file["seven"] = df_input_file["seven"].fillna("£0.0")
        print("replace nan values with the £0.0 in column seven: \n{}".format(df_input_file))
        print()

        # remove the first character (English pound symbol) in column seven
        df_input_file["seven"] = df_input_file["seven"].map(lambda x: str(x)[1:])
        print("remove the first character (English pound symbol) in column seven: \n{}".format(df_input_file))
        print()

        # replace the abbreviations in column eight with their full names
        df_input_file["eight"] = df_input_file["eight"].replace(to_replace=dict(
            BMC="BioMed Central",
            ACS="American Chemical Society",
            BPS="Biophysical Society",
            CJS="Cadmus Journal Services",
            FM="Frontiers Media"), inplace=True)
        print("substitute the abbreviation in column eight: \n{}".format(df_input_file))
        print()

        # drop the column eight from the data frame and keep the rest of the columns in the data frame
        x = df_input_file.drop(labels="eight", axis=1)
        print("x: labels by dropping column eight: \n{}".format(x))
        print()

        # select the first six columns from the data frame and keep them in a new data frame x
        x = df_input_file.iloc[:, 0:6].values
        print("x: labels selection by using index location method ilo(): \n{}".format(x))
        print()

        # select the column eight from the data frame and keep it in a new data frame y 
        y = df_input_file["eight"]
        print("y: target selection by column eight: \n{}".format(y))
        print()

        # select the column eight from the data frame and keep it in a new data frame y by using index location method ilo()
        y = df_input_file.iloc[:, 7].values
        print("y: target selection by using index location method ilo(): \n{}".format(y))
        print()

        # save the cleaned data frame into a new csv file
        df_input_file.to_csv(output_file_path, encoding="utf-8")
        print("the output file has been created successfully: {}".format(output_file_path))
        print()

    def sp_exc_result():
        '''
        scipy library is for scientific computing, which provides a wide range of functions and algorithms for scientific and technical computing, 
        including optimization, integration, interpolation, signal processing, linear algebra, and more.
        '''
        print("using scipy library for scientific computing:")

        def function_defined(x):
            return np.cos(x)
        
        # example 1: calculate first and second kind bessel functions
        alpha = 0
        x = 0.0
        print("first kind bessel function")
        print("J_{}({}) = {}".format(alpha, x, jn(alpha, x)))
        x = 1.0
        print("second kind bessel function")
        print("Y_{}({}) = {}".format(alpha, x, yn(alpha, x)))

        # plot four bessel functions
        x = np.linspace(0, 10, 100)
        fig, ax = plt.subplots()
        for alpha in range(4):
            ax.plot(x, jn(alpha, x), label=r"J$_{}(x)$".format(alpha))
        ax.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Bessel Functions")
        plt.show()

        # example 2: calculate definite integral
        a = 0
        b = 1
        integral_value, absolute_error = quad(function_defined, a, b)
        print("integral value: {} \nabsolute error: {}".format(integral_value, absolute_error))
        
        # example 3: linear and cubic functions interpolation
        n = np.arange(0, 10)
        x = np.linspace(0, 9, 100)

        # set the actual function values for x to compare with the interpolation results
        y_actual = function_defined(x)  
        
        # generate random experiment data by adding random noise to the actual function values at the points in n, 
        # which simulates the variability and uncertainty in real-world data, and can be used to evaluate the performance of 
        # interpolation methods
        y_experiment = function_defined(n) + 0.1 * np.random.randn(len(n))
        linear_interpolation = interp1d(n, y_experiment, kind="linear")

        # get linear interpolation values for x by using the linear interpolation function created with the interp1d function of 
        # scipy library, which takes the points in n and the corresponding experiment values as input, and returns a function 
        # that can be used to compute the interpolated values for any given x
        y_linear_interpolation = linear_interpolation(x)
        cubic_interpolation = interp1d(n, y_experiment, kind="cubic")

        # get cubic interpolation values for x by using the cubic interpolation function created with the interp1d function of 
        # scipy library, which takes the points in n and the corresponding experiment values as input, and returns a function 
        # that can be used to compute the interpolated values for any given x
        y_cubic_interpolation = cubic_interpolation(x)
        
        # plot y actual, experiment, linear and cubic interpolation values for x by using the plot function of matplotlib library, 
        # which creates a line plot of the given x and y values, and can be used to visualize the performance of interpolation methods 
        # in approximating the actual function values based on the experiment data
        fig, ax = plt.subplots(figsize=(10,4))
        ax.plot(n, y_experiment, "bs", label="experiment data")
        ax.plot(x, y_actual, "k", lw=2, label="actual function")
        ax.plot(x, y_linear_interpolation, "r", label="linear interpolation")
        ax.plot(x, y_cubic_interpolation, "g", label="cubic interpolation")
        ax.legend(loc=3)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Functions Interpolation Example")
        plt.show()

    choice = input("Numpy, Pandas or Scipy: ")
    if choice == "Numpy":     
        np_exc_result()
    elif choice == "Pandas":
        pd_exc_result()
    elif choice == "Scipy":
        sp_exc_result()
    else:
        print("invalid choice, please choose Numpy, Pandas or Scipy ")


if __name__ == '__main__':
    main()
