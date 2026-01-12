# Lumina Fashion Group: End-to-End Retail Analytics Pipeline 👗📊

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

## 📊 Project Overview
This project transforms fragmented retail data into a strategic analytical engine. As an **aspiring Data Scientist**, I leveraged mathematical rigor to unify sales, customer, product, and store domains, identifying critical inefficiencies in discount strategies and seasonal inventory management.

---

## 🏗️ Data Architecture: The Star Schema
To ensure analytical scalability, I transformed the raw CSV datasets into a **Relational Star Schema**. This architecture decouples quantitative metrics from descriptive attributes, optimizing query performance and data integrity.

### 🖼️ Visual Entity-Relationship Diagram (ERD)
<p align="center">
  <img src="images/star_schema.png" alt="Star Schema Architecture" width="600">
</p>

### 🗄️ Relational Design
- **Fact Table (`sales_data`):** Centralizes transactional metrics (Quantity, Discount, Returns).
- **Dimension Tables:** `product_data`, `store_data`, and `customer_data` provide the granular context needed for multidimensional analysis (Color, Category, Region, Age).

### 🛠️ The Master Analytical Query (ETL Logic)
I developed a robust SQL pipeline to handle data fragmentation and "dirty" entries found in the raw files (e.g., corrupted categories or missing IDs):

```sql
SELECT 
    s.transaction_id,
    s.date::DATE, 
    -- Handling missing Customer IDs to prevent data loss (Data Robustness)
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

---

## 🎯 High-Impact Insights (The "Hook")

> [!IMPORTANT]
> **Discount Inelasticity Detected:** Statistical analysis proved that discounts >20% showed a near-zero correlation with transaction volume. This indicates that margins were being sacrificed without a significant uplift in sales, leading to a recommendation for **volume-based bundles** instead of flat discounts.

* **Hero Products:** Identified "White" staples in Accessories and Dresses as the core revenue drivers across all regions.
* **Seasonality Misalignment:** Detected a 2-month lag between product "Season" attributes and actual consumer purchase behavior, suggesting a recalibration of clearance windows.

---

## 📊 Visual Intelligence

### Seasonal Sales Velocity
Analysis of transaction density by month vs. product season:
![Seasonal Analysis](https://github.com/JesusAHB25/Lumina-Fashion-Group-End-to-End-Retail-Analytics-Pipeline/blob/main/images/Sales%20Count%20per%20Month%20&%20Season.png?raw=true)

### Product Attribute Correlation (Heatmap)
Identifying high-performing color/category clusters:
![Category Color Heatmap](https://github.com/JesusAHB25/Lumina-Fashion-Group-End-to-End-Retail-Analytics-Pipeline/blob/main/images/Sales%20Count%20by%20Category%20and%20Color.png?raw=true)

---

## 📖 Executive Reporting (Notion)

The technical code is only half the story. The complete **Executive Case Study**, including the full strategic roadmap and data architecture diagrams, is documented in Notion.

[![Notion](https://img.shields.io/badge/Notion-Full_Strategic_Report-black?style=for-the-badge&logo=notion)](https://purring-sailboat-492.notion.site/Lumina-Fashion-Group-Retail-Analytics-End-to-End-Pipeline-2b01d3119ed08066b5f9f147da60599c?source=copy_link)

---

## 🛠️ Tech Stack & Requirements
* **Core:** Python 3.13, SQL (PostgreSQL logic).
* **Libraries:** Pandas, Seaborn, Matplotlib, SQLAlchemy.
* **Environment:** Jupyter Notebooks.

### Quick Start
1. `git clone https://github.com/JesusAHB25/Lumina-Fashion-Group-End-to-End-Retail-Analytics-Pipeline.git`
2. `pip install -r requirements.txt`
3. Open `Lumina Fashion Group Analysis.ipynb`

---
*Developed by **Jesús** | Mathematics Student & Aspiring Data Scientist 🤖🧿*
