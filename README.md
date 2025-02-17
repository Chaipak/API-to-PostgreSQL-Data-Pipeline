# 📱 API-to-PostgreSQL Pipeline 🚀

### **Fetch API Data → Process it → Store it in PostgreSQL**

## **📌 Overview**

This project automates the process of **fetching data from an API**, **cleaning the data**, and **storing it in a PostgreSQL database**.\
It is designed for **one-time or scheduled execution**, making it useful for data engineering workflows.

---

## **🛠️ Tech Stack**

- **Python** (Main programming language)
- **PostgreSQL** (Database)
- **Requests** (API fetching)
- **psycopg2** (PostgreSQL connector)
- **cron** (For automation on Linux/macOS)

---

## **📂 Project Structure**

```
API-to-PostgreSQL-Pipeline/
├── fetch_api.py        # Fetches data from an API
├── process_data.py     # Cleans and processes data
├── database.py         # Connects to PostgreSQL, creates table, inserts data
├── main.py             # Orchestrates the entire pipeline
├── config.py           # Stores database credentials (ignored in Git)
├── .gitignore          # Prevents tracking sensitive files
├── requirements.txt    # List of Python dependencies
└── README.md           # Documentation
```

---

## **⚡ How to Run Locally**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/your-username/API-to-PostgreSQL-Pipeline.git
cd API-to-PostgreSQL-Pipeline
```

### **2️⃣ Set Up a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up PostgreSQL Database**

1. Open PostgreSQL:
   ```bash
   psql -U your_username
   ```
2. Create the database:
   ```sql
   CREATE DATABASE APIProject;
   ```

### **5️⃣ Update **``** with Your Credentials**

```python
DB_CONFIG = {
    "dbname": "APIProject",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"
}
```

### **6️⃣ Run the Pipeline**

```bash
python main.py
```

👉 **Expected Output:** Data will be fetched from the API, cleaned, and stored in PostgreSQL.

---

## **🔦 How to Check Data in PostgreSQL**

```bash
psql -U your_username -d APIProject
```

Then, run:

```sql
SELECT * FROM posts LIMIT 5;
```

---

## **⏳ Automate the Process**

### **🔄 Run **``** Automatically Every Day**

#### **🖥️ macOS/Linux (Using **``**)**

1. Open the cron editor:
   ```bash
   crontab -e
   ```
2. Add this line (runs daily at 9 AM):
   ```
   0 9 * * * /Users/users/Desktop/Data\ Engineer/API-to-PostgreSQL-Pipeline/venv/bin/python /Users/users/Desktop/Data\ Engineer/API-to-PostgreSQL-Pipeline/main.py
   ```

---

## **📊 Database Schema**

| Column   | Type   | Description  |
| -------- | ------ | ------------ |
| id       | SERIAL | Primary Key  |
| user\_id | INT    | API User ID  |
| title    | TEXT   | Post Title   |
| body     | TEXT   | Post Content |

---

## **🌍 Future Improvements**

🔹 Support multiple APIs\
🔹 Deploy to cloud (AWS, Heroku, Railway.app)\
🔹 Add logging for better debugging

---

## **📝 License**

This project is open-source under the **MIT License**.

---

### **🚀 Feel free to contribute!**

If you find this useful, ⭐ **Star this repo** and feel free to submit **pull requests!** 😊

