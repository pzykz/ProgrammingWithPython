# Database Access libraries 'CRUD' Create, read, update, delete
from numpy import equal, where
import sqlalchemy as sa
import pymysql
import sqlalchemy as db

def main():
    def create_db():
        # get sqlalchemy and pymysql libraries version
        print("sqlalchemy version: {}".format(sa.__version__))
        print("pymysql version: {}".format(pymysql.__version__))

        # get engine object using pymysql driver for mysql
        engine = db.create_engine('mysql+pymysql://root:7233@localhost:3306/movie')
        # get connection object
        connection = engine.connect()
        # get meta data object
        metadata = db.MetaData()
        # set actor creation script table
        actor = db.Table("actor", metadata,
                        db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
                        db.Column("first_name", db.String(50), nullable=False),
                        db.Column("last_name", db.String(50), nullable=False),
                        db.Column("age", db.Integer, nullable=False),
                        db.Column("date_of_birth", db.Date, nullable=False),
                        db.Column("active", db.Boolean, nullable=False))
        # create actor table and stores the information in metadata
        metadata.create_all(engine)
        print("Database and table created successfully.")
    
    
    def add_data():
        # get engine object using pymysql driver for mysql
        engine = db.create_engine("mysql+pymysql://root:7233@localhost:3306/movie")
        # # get connection object
        # connection = engine.connect()
        # get metadata object
        meta_data = db.MetaData()
        # get actor table definitio
        actor_table = db.Table("actor", meta_data, #autoload=True, 
                               autoload_with=engine)
        # set data list
        data_list = [
                    {"first_name":"John", "last_name":"Smith", "age":50, "date_of_birth":"1969-04-05","active":True},
                    {"first_name":"Brian", "last_name":"Morgan", "age":38, "date_of_birth":"1981-02-11", "active":True},
            {"first_name": "David", "last_name": "White", "age": 77, "date_of_birth": "1942-06-30", "active": False}]
        # set the insert statement
        sql_query = db.insert(actor_table).values(data_list)
        # content manager to securely close and open the connection
        with engine.connect() as connection:
            # execute the insert statement
            connection.execute(sql_query)
            connection.commit()
        
        print("Data added successfully.")
    
    
    def read_data():
        # get engine object using pymysql driver for mysql
        engine = db.create_engine("mysql+pymysql://root:7233@localhost:3306/movie")
        # get connection object
        connection = engine.connect()
        # get metadata object
        meta_data = db.MetaData()
        # get actor table definition
        actor_table = db.Table("actor", meta_data, #autoload=True, 
                               autoload_with=engine)
        # set the select statement
        select_actor = db.select(actor_table)
        # execute the select statement
        dataset = connection.execute(select_actor).fetchall()
        # print the results
        for row in dataset:
            print(f"Row: {row}")
        print("Data read successfully.")

    def update_data():
        # get engine object using pymysql driver for mysql
        engine = db.create_engine("mysql+pymysql://root:7233@localhost:3306/movie")
        # get connection object
        connection = engine.connect()
        # get metadata object
        meta_data = db.MetaData()
        # get actor table definition
        actor_table = db.Table("actor", meta_data, #autoload=True, 
                               autoload_with=engine)
        # set update sql statement. update column 'active' to true where id is equal to 18 
        sql_query = db.update(actor_table).values(active=True).where(actor_table.columns.id == 18)
        # execute the update statement
        connection.execute(sql_query)
        connection.commit()
        print("Data updated successfully.")

    def del_data():
        # get engine object using pymysql driver for mysql
        engine = db.create_engine("mysql+pymysql://root:7233@localhost:3306/movie")
        # get connection object
        connection = engine.connect()
        # get metadata object
        meta_data = db.MetaData()
        # get actor table definition
        actor_table = db.Table("actor", meta_data, #autoload=True, 
                               autoload_with=engine)
        # set delete sql statement. delete the row where id is equal to 18 
        sql_query = db.delete(actor_table).where(actor_table.columns.id >= 1)
        # execute the delete statement
        connection.execute(sql_query)
        connection.commit()
        print("Data deleted successfully.")


    choice = input("Create DB, Add data, Read data, Update data, Delete data ?")
    if choice == "Create DB":
        create_db()
    elif choice == "Add data":
        add_data()
    elif choice == "Read data":
        read_data()
    elif choice == "Update data":
        update_data()
    elif choice == "Delete data":
        del_data()
    else:
        print("Invalid choice, please choose Create DB, Add data, Read data, Update data, or Delete data.")


if __name__ == '__main__':
    main()
