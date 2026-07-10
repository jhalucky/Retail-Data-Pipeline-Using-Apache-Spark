# 🚀 Retail Data Pipeline using Apache Spark

A production-style Data Engineering project that demonstrates how to build an end-to-end ETL pipeline using **Apache Spark**, perform data validation and transformations, create an analytical **Fact Sales** table, generate business insights, and store optimized datasets in **Apache Parquet** format.

---

## 📌 Project Overview

This project simulates a real-world retail company's data pipeline.

Synthetic retail datasets are generated using the **Faker** library, processed using **Apache Spark**, validated, transformed, joined into a single analytical dataset, and stored in **Parquet** format for efficient querying.

The project also includes multiple business analytics reports and Spark performance optimizations.

---

# 🏗 Architecture

<p align="center">
    <img src="images/architecture.png" width="900">
</p>

---

# 🔄 Pipeline Flow

```
Raw CSV Files
       │
       ▼
Apache Spark Session
       │
       ▼
Data Validation
       │
       ▼
Data Cleaning
       │
       ▼
Data Transformation
       │
       ▼
Multi-table Joins
       │
       ▼
Fact Sales DataFrame
       │
       ├─────────────► Business Analytics
       │
       ├─────────────► Spark SQL
       │
       ▼
Apache Parquet
```

---

# 📂 Project Structure

```
Retail-Data-Lakehouse-Pipeline
│
├── data
│   ├── raw
│   └── processed
│
├── experiments
│
├── logs
│
├── sql
│
├── src
│   ├── analytics
│   ├── config
│   ├── extract
│   ├── generate
│   ├── load
│   ├── transform
│   └── validate
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Processing Engine | Apache Spark |
| Storage Format | Apache Parquet |
| Synthetic Data | Faker |
| Data Processing | PySpark |
| Version Control | Git & GitHub |

---

# 📊 Datasets

The project generates synthetic retail datasets.

- Customers
- Orders
- Order Items
- Products
- Payments

Total Records:

- Customers : 1,000
- Orders : 1,000
- Order Items : 1,000
- Products : 1,000
- Payments : 1,000

---

# ⚙ Features

## Data Generation

- Generate synthetic retail datasets
- Maintain primary and foreign key relationships
- Modular data generators

---

## Data Validation

- Missing Value Detection
- Duplicate Row Detection
- Duplicate Primary Key Detection

---

## Data Cleaning

- Remove whitespace
- Standardize text case
- Email cleaning
- Phone number cleaning
- Data type conversion

---

## Data Transformation

- Multi-table joins
- Fact Sales table creation
- Sales Amount calculation

---

## Business Analytics

- Revenue by Category
- Revenue by State
- Monthly Revenue
- Top Selling Products
- Top Customers
- Payment Distribution
- Average Order Value

---

## Spark Optimizations

- Lazy Evaluation
- Cache
- Persist
- Repartition
- Coalesce
- Broadcast Join
- Explain Plan
- Spark SQL

---

# 💾 Storage

Final analytical data is stored in **Apache Parquet** format for:

- Faster reads
- Compression
- Columnar storage
- Schema preservation

---

# 📈 Sample Analytics

## Revenue by Category

<p align="center">
<img src="images/revenue_category.png">
</p>

---

## Top Products

<p align="center">
<img src="images/top_products.png">
</p>

---

## Monthly Revenue

<p align="center">
<img src="images/monthly_revenue.png">
</p>

---

# 🚀 How to Run

Clone Repository

```bash
git clone https://github.com/jhalucky/Retail-Data-Lakehouse-Pipeline.git
```

Go to project

```bash
cd Retail-Data-Lakehouse-Pipeline
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

# 📚 Spark Concepts Covered

- Spark Session
- DataFrames
- Transformations
- Actions
- Lazy Evaluation
- Joins
- Aggregations
- Broadcast Join
- Cache
- Persist
- Repartition
- Coalesce
- Explain Plan
- Spark SQL
- Apache Parquet

---

# 📖 Learning Outcomes

After completing this project, I learned:

- Building modular ETL pipelines
- Apache Spark DataFrame API
- Spark SQL
- Data validation strategies
- Fact table creation
- Business analytics using Spark
- Performance optimization techniques
- Efficient storage using Apache Parquet

---

# 🔮 Future Improvements

- AWS S3 Integration
- Snowflake Integration
- Delta Lake
- Databricks
- Apache Airflow Scheduling
- Power BI Dashboard
- Docker Support
- Unit Testing
- CI/CD Pipeline

---

# 👨‍💻 Author

**Lucky Jha**

GitHub: https://github.com/jhalucky

LinkedIn: https://www.linkedin.com/in/theluckyjha

---
