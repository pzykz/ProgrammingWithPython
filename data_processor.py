# data extraction from the output_data.scv to view the data in a more readable format
import pandas as pd

def process_data(file_path):
    # Read the CSV file into a DataFrame
    df = pd.DataFrame(pd.read_csv(file_path))

    # Display the first few rows of the DataFrame to understand its structure
    print("Data Preview before:")
    print(df)

    # data cleaning and processing steps can be added here as needed
    # give data frame named header to the data frame
    df.rename(columns={df.columns[0]: 'Index', df.columns[1]: 'One', df.columns[2]: 'Two', df.columns[3]: 'Three', df.columns[4]: 'Four', df.columns[5]: 'Five', df.columns[6]: 'Six', df.columns[7]: 'Seven', df.columns[8]: 'Eight'}, inplace=True)

    # sort the data by a specific column (e.g., 'column_name')
    df = df.sort_values(by=['Six'], ascending=False)
    
    # Save the processed data to a new CSV file
    processed_file_path = "processed_data.csv"
    df.to_csv(processed_file_path, index=False)
    print(f"Processed data saved to {processed_file_path}")

    print("Data Preview after:")
    print(df)

if __name__ == "__main__":
    # Specify the path to the input CSV file
    input_file_path = "output_data.csv"
    
    # Process the data
    process_data(input_file_path)