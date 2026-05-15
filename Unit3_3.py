# Machine learning libraries
from sklearn.tree import DecisionTreeClassifier #importing classification algorithm
from sklearn.cluster import KMeans #importing clustering algorithm

def main():
    def sk_exc_result():
        '''
        sklearn library is for machine learning, which provides a wide range of algorithms and tools for machine learning tasks, 
        including classification, regression, clustering, dimensionality reduction, and more.
        '''
        print("using sklearn library for machine learning:")
        print()

        def classification() -> None:  # Penguin data: [beak length, flipper length]
            X = [[39, 181],
                [50, 195],
                [46, 210],
                [38, 182]]
            # Known penguin species
            y= ["Adelie", "Chinstrap", "Gentoo", "Adelie"]
        
            # Create and train the classification model
            model= DecisionTreeClassifier()
            model.fit(X, y)

            # Predict the species of a new penguin
            prediction= model.predict([[48, 198]])
            print("Classification:")
            print("A new penguin with beak length 48 and flipper length 198 is predicted as: \n", prediction[0])
            print()

        def clustering():  # Penguin data: [beak length, flipper length] 
            X = [[39, 181],
                [40, 185],
                [50, 195],
                [51, 197],
                [46, 210],
                [47, 212]]
            # Create and train the clustering model
            model= KMeans(n_clusters=3, random_state=0)
            model.fit(X)
            print("Clustering:")
            print("Penguins are grouped into clusters like this: \n", model.labels_)
            print()

        classification()
        clustering()

    # def pd_exc_result():
    #     '''
    #     pandas library is for data manipulation and cleansing, which provides data structures and functions for working with structured data, 
    #     such as tabular data in the form of data frames, and offers powerful tools for data cleaning, transformation, and analysis.
    #     '''
    #     print("using pandas library for data manipulation and cleansing:")
    #     print()


    # def sp_exc_result():
    #     '''
    #     scipy library is for scientific computing, which provides a wide range of functions and algorithms for scientific and technical computing, 
    #     including optimization, integration, interpolation, signal processing, linear algebra, and more.
    #     '''
    #     print("using scipy library for scientific computing:")
    #     print()


    choice = input("Sklearn? (yes/no): ")
    if choice == "yes":
        sk_exc_result()
    # elif choice == "Keras":
    #     pd_exc_result()
    # elif choice == "Scipy":
    #     sp_exc_result()
    else:
        print("invalid choice, please choose Sklearn")


if __name__ == '__main__':
    main()
