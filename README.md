# Lumina Fashion Group: End-to-End Retail Analytics Pipeline 👗📊

<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-%234470AD.svg?style=for-the-badge&logo=Seaborn&logoColor=white" alt="Seaborn">
</p>

## 📈 High-Level Strategy & Insights
<p align="center">
   <a href="https://purring-sailboat-492.notion.site/Lumina-Fashion-Group-Retail-Analytics-End-to-End-Pipeline-2b01d3119ed08066b5f9f147da60599c?source=copy_link">
     <img src="https://img.shields.io/badge/Notion-View_Executive_Report-000000?style=for-the-badge&logo=notion&logoColor=white" alt="Notion Badge">
   </a>
   <br>
   <em>Visit the full case study for business recommendations and the strategic roadmap.</em>
 </p>

## 📊 Project Overview
This project transforms fragmented retail data into a strategic analytical engine. As a **Mathematics Student and Aspiring Data Scientist**, I leveraged mathematical rigor to unify sales, customer, product, and store domains. The objective was to build a robust data infrastructure to identify critical inefficiencies in discount strategies and seasonal inventory management.

## 🏗️ Phase 0: Data Engineering & Pre-Processing

### 🔬 Initial Data Audit (The "Dirty" Data)
Before any analysis, a deep audit was conducted to ensure data reliability and mathematical integrity:
* **Missing Values Detected:** 496 missing emails, 990 missing colors, and 1,844 missing `customer_id` entries in the Sales dataset.
* **Strategic Imputation:** Missing customer IDs were tagged as **"GUEST-001"**. This decision preserves total transaction volume (1,844 records) while preventing the skewing of CRM and Loyalty Program metrics.
* **Formatting:** Converted date strings into standardized ISO Datetime objects to enable precise time-series decomposition.

### 🏗️ Relational Architecture (Star Schema)
To ensure analytical scalability, I transformed raw CSV datasets into a **Relational Star Schema**. This architecture decouples quantitative metrics from descriptive attributes, optimizing query performance.

<p align="center">
  <img src="images/star_schema.png" alt="Star Schema Architecture" width="600">
</p>

### ⚙️ Automated ETL Migration
I implemented an automated ingestion layer using **SQLAlchemy** to migrate data from the local environment to a **PostgreSQL** instance, ensuring data type enforcement across 50,000+ records.

## 🛠️ Phase 1: Extraction & Integration (Master SQL)
I developed a robust SQL pipeline to handle data fragmentation at the source level. This "Master Query" performs multi-way JOINs and cleans corrupted entries before they reach the Python analytical environment:

```sql
SELECT 
    s.transaction_id,
    s.date::DATE, 
    -- Handling missing Customer IDs to prevent data loss
    COALESCE(s.customer_id, 'GUEST-001') as customer_id, 
    p.season,
    st.store_name,
    st.region,
    -- Data Sanitization: Replacing corrupted '???' strings with 'Other'
    REPLACE(p.category, '???', 'Other') as category, 
    COALESCE(p.color, 'Unspecified') as color, 
    s.quantity,
    p.list_price,
    -- Financial Normalization: Treating null discounts as zero for margin calculation
    COALESCE(s.discount, 0) as discount_pct, 
    (s.quantity * p.list_price) * (1 - COALESCE(s.discount, 0)) as net_revenue 
FROM sales s
LEFT JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id
JOIN stores st ON s.store_id = st.store_id;
```

## 🔬 Phase 2: Exploratory Data Analysis (EDA)

### 📈 Temporal Characteristics & Seasonality
* **Discovery:** Revenue remains stable month-over-month (~$2.5M), but analysis revealed a significant **"Season-Month Mismatch."**
* **Finding:** Products labeled as "Winter" or "Summer" sell at uniform rates regardless of the month, indicating an opportunity for more aggressive seasonal clearance strategies to optimize inventory turnover.

<p align="center">
  <img src="https://github.com/JesusAHB25/Lumina-Fashion-Group-End-to-End-Retail-Analytics-Pipeline/blob/main/images/Sales%20Count%20per%20Month%20&%20Season.png?raw=true" alt="Seasonal Analysis" width="750">
</p>

### 🎯 The Discount Elasticity Paradox (Technical "Hook")

> [!IMPORTANT]
> **Financial Insight:** By using **Median-based aggregation** to neutralize transaction outliers, I proved that discounts >20% showed a near-zero correlation with volume increase. The median quantity remained constant at **3 units**, proving that Lumina was sacrificing net margins without driving a proportional volume uplift.

<p align="center">
  <img src="https://github.com/JesusAHB25/Lumina-Fashion-Group-End-to-End-Retail-Analytics-Pipeline/blob/main/images/Total%20Net%20Revenue%20by%20Discount%20Percentage.png?raw=true" alt="Discount Elasticity Paradox" width="750">
</p>

### 🗺️ Geospatial & Attribute Performance
* **Hero Products:** Heatmap analysis identified **"White"** staples in Accessories and Dresses as the highest-frequency transaction clusters across the entire ecosystem.
* **Regional Balance:** Revenue is remarkably balanced across regions, with the **Online Store** performing at par with physical boutiques (~$2.43M), suggesting a high ceiling for digital-first scaling.

<p align="center">
  <img src="https://github.com/JesusAHB25/Lumina-Fashion-Group-End-to-End-Retail-Analytics-Pipeline/blob/main/images/Sales%20Count%20by%20Category%20and%20Color.png?raw=true" alt="Category Color Heatmap" width="750">
</p>

## 🛠️ Tech Stack & Requirements
* **Core:** Python 3.13, SQL (PostgreSQL logic).
* **Libraries:** Pandas, NumPy, Seaborn, Matplotlib, SQLAlchemy.
* **Environment:** Jupyter Notebooks.

## 🛠️ Setup & Quick Start
1. **Clone the repository**:  
   `git clone https://github.com/JesusAHB25/Lumina-Fashion-Group-End-to-End-Retail-Analytics-Pipeline.git`
2. **Install dependencies**:  
   `pip install -r requirements.txt`
3. **Configure your local PostgreSQL URL** in the notebook.
4. **Open Lumina Fashion Group Analysis.ipynb** and run the cells to replicate the pipeline.

## 📂 Repository Structure
```text
├── data/
│   └── 📄 Raw CSV files                         # Original datasets (Sales, Customers, etc.)
├── sql_queries/
│   └── 📄 master_query.sql                      # Complex JOINs and data extraction logic
├── src/
│   └── 📄 data_preprocessing.py                 # Modular Python functions (ETL & Cleaning)
│   └── 📄 eda.py                                # Statistical exploration and visualization logic
├── notebooks/
│   └── 📓 Lumina Fashion Group Analysis.ipynb   # Full implementation (Engineering + EDA)
├── images/
│   └── 🖼️ ERD diagrams, Heatmaps, and Trend plots
└── 📄 requirements.txt                          # Project dependencies (Pandas, SQLAlchemy, etc.)
```

---
*Developed by **Jesús** | Mathematics Student & Aspiring Data Scientist* 🤖🧿
