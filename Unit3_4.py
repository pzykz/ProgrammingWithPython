# Data Visualization libraries
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
import seaborn as sns
from bokeh.plotting import figure, output_file, show
# from bokeh.sampledata.iris import flowers 


def main():
    def mpl_exc_result():
        '''
        matplotlib library is for data visualization, which provides a wide range of plotting functions and tools for creating static, 
        animated, and interactive visualizations in Python.
        '''
        print("using matplotlib library for data visualization:")
        print()

        # x and y data list
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        
        style.use('ggplot')  # set plot style to ggplot

        # line plot example
        plt.plot(x, y, label="line plot example", linewidth=2)
        plt.legend()
        plt.grid(True, color="k")
        plt.ylabel('y axis')
        plt.xlabel('x axis')
        plt.title('Line Plot')
        plt.show()

        # bar chart vertical example
        plt.bar(x, y, label="bar chart vertical example", align='center')
        plt.legend()
        plt.grid(True, color="k")
        plt.ylabel('y axis')
        plt.xlabel('x axis')
        plt.title('Bar Chart Vertical')
        plt.show()

        # bar chart horizontal example
        plt.barh(x, y, label="bar chart horizontal example", align='center')
        plt.legend()
        plt.grid(True, color="k")
        plt.ylabel('y axis')
        plt.xlabel('x axis')
        plt.title('Bar Chart Horizontal')
        plt.show()

        # scatter plot example
        plt.scatter(x, y, label="scatter plot example")
        plt.legend()
        plt.grid(True, color="k")
        plt.ylabel('y axis')
        plt.xlabel('x axis')
        plt.title('Scatter Plot')
        plt.show()

        # histogram plot example
        mu, sigma = 100, 15
        x = mu + sigma * np.random.randn(10000)
        # print(x)
        n, bins, patches = plt.hist(x, 50, density=1, facecolor='r', alpha=0.75, label="histogram plot example")
        plt.text(45, 0.028, r'$\mu=100,\ \sigma=15$')
        plt.axis([40, 160, 0, 0.03])
        plt.legend()
        plt.grid(True, color="k")
        plt.xlabel("x")
        plt.ylabel("P(x)")
        plt.title("Histogram Plot")
        plt.show()
        
    def sns_exc_result():
        '''
        Seaborn library is for data manipulation and cleansing, which provides data structures and functions for working with structured data,
        such as tabular data in the form of data frames, and offers powerful tools for data cleaning, transformation, and analysis.
        '''
        print("using seaborn library for data manipulation and cleansing:")
        print()

        iris_data = sns.load_dataset("iris")
        print(iris_data.head())
        
        style.use('ggplot')  # set plot style to ggplot

        # swarm plot example
        sns.swarmplot(x="species", y="petal_length", data=iris_data)
        plt.text(40, 7, "abc")
        plt.ylabel("petal length, cm")
        plt.xlabel("species")
        plt.title("Species vs. Petal Length")
        plt.show()        
        
        # # factor plot example
        # sns.factorplot("species", "petal_length", data=iris_data, kind="bar", palette="muted", legend=False)
        # plt.ylabel("petal length, cm")
        # plt.xlabel("species")
        # plt.title("Species vs. Petal Length")
        # plt.show()

        # box plot example
        sns.boxplot(x="species", y="petal_length", data=iris_data)
        plt.ylabel("petal length, cm")
        plt.xlabel("species")
        plt.title("Species vs. Petal Length")
        plt.show()
        
        # pair plot example
        sns.pairplot(iris_data, hue="species", size=2)
        plt.ylabel("petal length, cm")
        plt.xlabel("species")
        plt.show()


    def bo_exc_result():
        '''
        Bokeh library is for creating interactive visualizations, which provides a wide range of tools for building custom web-based plots 
        and dashboards.
        '''
        print("using Bokeh library for creating interactive visualizations:")
        print()

        # line plot example
        x = [1, 2, 3, 4, 5]
        y = [5, 6, 1, 3, 4]
        output_file("line_example.html")
        plot = figure(title="Line Plot", x_axis_label="x axis", y_axis_label="y axis")
        plot.line(x, y, # legend="line example", 
                  line_width=2)
        show(plot)

        # cos(x) function example
        output_file("cosx_example.html")
        x = np.linspace(-6, 6, 100)
        y = np.cos(x)
        plot = figure(width=500, height=500, title="Cos(x) Plot", x_axis_label="x axis", y_axis_label="y axis")
        plot.circle(x, y, size=7, color="firebrick", alpha=0.5#, legend="cos(x) example"
                    )
        show(plot)

        # bar chart example
        output_file("barchart_example.html")
        teams = ["A", "B", "C", "D", "E", "F"]
        plot = figure(x_range=teams, height=500, title="Bar Chart Plot", x_axis_label="teams", y_axis_label="values")
        plot.vbar(x=teams, top=[4, 2, 3, 1, 3, 5], width=0.6#, legend="bar chart example"
                  )
        show(plot)
        
        # # iris flowers scatter example
        # output_file("iris_scatter_example.html")
        # colormap = {"setosa": "orange", "versicolor": "blue", "virginica": "gray"}
        # colors = [colormap[x] for x in flowers['species']]
        # plot = figure(title="Iris Flowers Scatter Plot", x_axis_label="petal length", y_axis_label="petal width")
        # plot.circle(flowers["petal_length"], flowers["petal_width"], color=colors, fill_alpha=0.2, size=10, legend="scatter plot example")
        # show(plot)

    choice = input("Matplotlib, Seaborn or Bokeh? ")
    if choice == "Matplotlib":
        mpl_exc_result()
    elif choice == "Seaborn":
        sns_exc_result()
    elif choice == "Bokeh":
        bo_exc_result()
    else:
        print("invalid choice, please choose Matplotlib, Seaborn or Bokeh")


if __name__ == '__main__':
    main()
