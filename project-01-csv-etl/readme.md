# 📊 Project 1: Sales Data ETL Pipeline

## 📝 Overview
This project implements a simple **ETL (Extract, Transform, Load) pipeline** that processes sales data from CSV files.  
The pipeline cleans and transforms the data, then exports the results in multiple formats for further use.

---

## 📂 Workflow
1. **Extract** – Read raw sales data from CSV files using `pandas`.
2. **Transform** – Clean, validate, and enrich the dataset:
   - Remove duplicates  
   - Handle missing values  
   - Convert data types  
   - Add calculated fields  
   - Apply filtering rules
3. **Load** – Save the transformed data to multiple output formats (`.csv`, `.json`).

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
python sales_etl.py
