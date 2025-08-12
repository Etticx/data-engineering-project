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
- **Data filtering** – Keeps only recent sales data

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
- **JSON & CSV** modules for output formats

---

## 🚀 How to Run
```bash
# Install dependencies
pip install pandas

# Run the ETL pipeline
python sales_data_etl_pipeline.py
