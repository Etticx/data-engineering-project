# 📊 Project 1: Sales Data ETL Pipeline

## 📝 Overview
This project implements a simple **ETL (Extract, Transform, Load) pipeline** that processes sales data from CSV files.  
The pipeline cleans and transforms the data, then exports the results in multiple formats for further use.

---

## 🔄 The ETL Process

### **1️⃣ Extract**
- Reads sales data from a CSV file using `pandas`
- Handles file errors gracefully with basic error handling

### **2️⃣ Transform**
- **Remove duplicates** – Eliminates duplicate records
- **Handle missing data** – Fills missing customer names, removes rows with missing critical data
- **Data type conversion** – Converts date fields, ensures numeric types are consistent
- **Calculated fields** – Adds `total_amount`, `year`, and `month` columns
- **Data filtering** – Keeps sales dated in the current calendar year or the previous year

### **3️⃣ Load**
- Saves cleaned data in **CSV** format
- Exports to **JSON** for flexibility
- Generates **summary statistics** for quick insights

---

## 💡 What I Learned
- 📥 **Reading CSV files** with `pandas`  
- 🧹 **Data cleaning**: removing duplicates, handling missing values  
- 🔄 **Data transformation**: type conversions, calculated fields  
- 🔍 **Data filtering and validation**  
- 💾 **Exporting data** to different formats (CSV, JSON)  
- ⚠️ **Basic error handling** in Python scripts

---

## 🛠 Tools & Libraries
- **Python 3.x**
- **Pandas** for data processing
- **NumPy** for generating reproducible sample data
- **Pandas CSV/JSON exporters** for writing the results

---

## 🚀 How to Run

Run these commands from the repository root:

```bash
cd project-01-csv-etl
python -m pip install pandas numpy
python sales_data_etl_pipeline.py
```

Use an activated Python virtual environment to keep the dependencies separate from other projects.

### Input and generated files

The script generates its own synthetic sales data on every run; you do not need to download a CSV or configure a database.

Paths are relative to the directory where you run the script. With the commands above, it writes:

- `sample_sales_data.csv`: generated input data.
- `Output_Sales_Data_AfterETL/cleaned_sales_data.csv`: transformed sales in CSV format.
- `Output_Sales_Data_AfterETL/cleaned_sales_data.json`: the same transformed records in JSON format.

Running the script again overwrites these files. Keep any personal input or results elsewhere.

The terminal also prints row counts, total revenue, average sale amount, and the top five products by quantity sold.

### Why the number of results changes over time

The sample generator uses dates from 2024–2025, while the transformation retains the current calendar year and the previous year. This is a calendar-year filter, rather than a rolling 24-month window. The saved results therefore depend on the year when you run the example, and can be empty once both sample years fall outside that filter. To experiment with more recent sales, adjust the sample date range and its matching random index bound in `generate_sample_data()`.
