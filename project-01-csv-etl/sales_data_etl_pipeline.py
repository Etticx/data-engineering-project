import pandas as pd
import numpy as np
from datetime import datetime
import os

#0 Data Generate (just for this project example)
def generate_sample_data():
    np.random.seed(42)
    customers = ["Alice", "Bob", "Carol", "Fariz", "Frank", None, "Faiq"]
    products = ["Laptop", "Mouse", "Montior", "Webcam", "Keyboard", "Headphones"]
    data = []
    for i in range(100):
        data.append({
            'sale_id': f'S{i+1:03d}',
            'customer_name': np.random.choice(customers),
            'product': np.random.choice(products),
            'quantity': np.random.randint(1, 10),
            'price': round(np.random.uniform(10,500), 2),
            'sale_date': pd.date_range('2024-01-01', '2025-12-31', freq='D')[np.random.randint(0,730)]
        })
    df = pd.DataFrame(data)
    df = pd.concat([df, df.head(5)], ignore_index=True)
    return df


#1 Data Extraction
def extract_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Data Extracted Sucessfully. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} is not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

#2 Data Transform
def transform_data(df):
    df_clean = df.copy() # make a copy just incase to not modify the original dataframe
    print("Starting data transformation...")

    #1. Remove Duplicates
    initial_rows = len(df_clean)
    df_clean = df_clean.drop_duplicates()
    print(f"Removed {initial_rows - len(df_clean)} duplicated rows")

    #2. Handle Missing Values
    df_clean['customer_name'] = df_clean['customer_name'].fillna("Unknown")

    #3. Remove rows when critial data missing (in this dataset example is product, quantity, and price)
    df_clean = df_clean.dropna(subset=["product", "quantity", "price"])

    #4. Data type conversions
    df_clean['sale_date'] = pd.to_datetime(df_clean['sale_date'])
    df_clean['quantity'] = df_clean['quantity'].astype(int)
    df_clean['price'] = df_clean['price'].astype(float)

    #5 Create new calculated columns (to make this project has meaningful outcomes)
    df_clean['total_amount'] = df_clean['quantity'] * df_clean['price']
    df_clean['year'] = df_clean['sale_date'].dt.year
    df_clean['month'] = df_clean['sale_date'].dt.month

    #6 (Additional) Filter relevant data (sales data from last 2 years)
    current_year = datetime.now().year
    df_clean = df_clean[df_clean['year'] >= current_year - 1]
    print(f"Transformation Completed. Final Shape: {df_clean.shape}")
    return df_clean


#3 Load Data
def load_data(df, output_path, format_type='csv'):
    try:
        if format_type.lower() == 'csv':
            df.to_csv(output_path, index=False)
            print(f"Data saved to {output_path}")
        elif format_type.lower() == 'json':
            df.to_json(output_path, orient='records', date_format='iso')
            print(f"Data saved to {output_path}")
        else:
            print(f"Format {format_type} is not supported.")
    except Exception as e:
        print(f"Error saving data: {e}")




### MAIN BLOCK #####
def main():
    print("===== SALES DATA ETL PIPELINE =====")

    #Create Sample Data
    sample_df = generate_sample_data()
    sample_df.to_csv("sample_sales_data.csv", index=False)
    print("Sample Data created: sample_sales_data.csv")


    #ETL PROCESSES
    #1. Extract
    raw_data = extract_data("sample_sales_data.csv")

    if raw_data is not None:
        #2. Transform
        cleaned_data = transform_data(raw_data)
        #3. Load
        os.makedirs('Output_Sales_Data_AfterETL', exist_ok=True)

        #Save in json and csv
        load_data(cleaned_data, "Output_Sales_Data_AfterETL/cleaned_sales_data.csv", 'csv')
        load_data(cleaned_data, "Output_Sales_Data_AfterETL/cleaned_sales_data.json", 'json')


        # Show Summary Statistics
        print("\n=========== DATA SUMMARY ============")
        print(f"Total Sales: {len(cleaned_data)}")
        print(f"Total Revenue: ${cleaned_data['total_amount'].sum():,.2f}")
        print(f"Average sale amount: ${cleaned_data['total_amount'].mean():,.2f}")
        print("\nTop 5 products by quantity sold: ")
        print(cleaned_data.groupby('product')['quantity'].sum().sort_values(ascending=False).head())


if __name__ == "__main__":
    main()