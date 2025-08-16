# 📊 Project 2: YouTube Trending Data Pipeline

## 📝 Overview
This project implements an **ETL (Extract, Transform, Load) pipeline** that fetches trending YouTube video data from the YouTube API.  
The pipeline processes the data, cleans and transforms it, and then loads it into a PostgreSQL database for further analysis.

---

## 🔄 The ETL Process

### **1️⃣ Extract**
- Fetches trending video data using the **YouTube API** (`googleapiclient.discovery`)  
- Handles **API authentication** with a secure API key placeholder  
- Extracts key fields like `video_id`, `title`, `channel_title`, `published_at`, `views`, `likes`, and `comments`

### **2️⃣ Transform**
- Converts `published_at` to a **proper datetime format** using `pandas`  
- Filters videos with **views greater than 0**  
- Cleans and structures the data for database ingestion  

### **3️⃣ Load**
- Loads the processed data into **PostgreSQL** using `SQLAlchemy`  
- Table: `trending_videos`  
- Schema: `public`  
- Supports **replace mode** to refresh data on each run  

---

## 💡 What I Learned
- 📥 **Fetching data from APIs** securely using API keys  
- 🧹 **Data cleaning**: handling zero views, formatting datetime fields  
- 🔄 **Data transformation** with `pandas`  
- 💾 **Loading data into PostgreSQL** using `SQLAlchemy`  
- ⚠️ **Secure key management**: using placeholders to avoid leaking credentials  

---

## 🛠 Tools & Libraries
- **Python 3.x**  
- **Pandas** for data processing  
- **Google API Client** (`googleapiclient`) for YouTube API access  
- **SQLAlchemy** for PostgreSQL database interaction  

---

## 🚀 How to Run
```bash
# Install dependencies
pip install pandas google-api-python-client sqlalchemy psycopg2-binary

# Set your API key and PostgreSQL connection as environment variables
export YOUTUBE_API_KEY="YOUR_API_KEY"
export POSTGRES_PATH="postgresql+psycopg2://user:password@localhost:5432/your_db"

# Run the ETL pipeline
python project-02-youtubetrending.py
