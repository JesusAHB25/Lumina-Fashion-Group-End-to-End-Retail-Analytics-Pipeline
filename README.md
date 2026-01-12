# Lumina Fashion Group: End-to-End Retail Analytics Pipeline 👗📊

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

## 📊 Project Overview
This project transforms fragmented retail data into a strategic analytical engine. As an **aspiring Data Scientist**, I leveraged mathematical rigor to unify sales, customer, product, and store domains, identifying critical inefficiencies in discount strategies and seasonal inventory management.

---

## 🏗️ Architecture & Pipeline
I designed a robust data lifecycle divided into four distinct phases:

1. **Extraction & Relational Integration:** - Migration of decoupled CSV datasets into a **Star Schema** architecture.
   - Used **SQLAlchemy** to enforce referential integrity between Fact (Sales) and Dimension (Customers, Products, Stores) tables.
2. **Data Sanitization & Rigor:** - Managed **1,000+ null values** using a targeted imputation strategy (COALESCE logic) to prevent statistical bias.
   - Standardized temporal data to ensure precision in time-series analysis.
3. **Advanced EDA:** - Multidimensional analysis focusing on regional performance and attribute correlation.
4. **Strategic Optimization:** - Translating Python-driven findings into high-impact business recommendations.

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
