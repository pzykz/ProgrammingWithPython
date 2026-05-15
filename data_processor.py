# data extraction from the output_data.scv to view the data in a more readable format
import pandas as pd

def process_data(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame to understand its structure
    print("Data Preview:")
    print(df.head())

    # data cleaning and processing steps can be added here as needed
    # For example, if there are any missing values, we can fill them or drop them
    # drop first column
    df = df.drop(df.columns[0], axis=1)

    # Save the processed data to a new CSV file
    processed_file_path = "processed_data.csv"
    df.to_csv(processed_file_path, index=False)
    print(f"Processed data saved to {processed_file_path}")

if __name__ == "__main__":
    # Specify the path to the input CSV file
    input_file_path = "output_data.csv"
    
    # Process the data
    process_data(input_file_path)