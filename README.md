# Lumina Fashion Group: End-to-End Retail Analytics Pipeline

## 📊 Project Overview
This project transforms fragmented retail data into a strategic analytical engine. By integrating sales, customer, product, and store data, I identified key inefficiencies in discount strategies and seasonal inventory management, providing actionable recommendations to optimize net revenue.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Libraries:** Pandas, Seaborn, Matplotlib, SQLAlchemy
* **Database Logic:** SQL (PostgreSQL compatible)
* **Documentation:** Notion (Executive Reporting)

## 🏗️ Architecture & Pipeline
The project is divided into four distinct phases:

1.  **Extraction & Integration:** Migration of flat CSV files into a Relational Data Model (Star Schema) using SQLAlchemy and SQL JOINs.
2.  **Data Cleaning:** Implementation of a cleaning pipeline to handle missing values (COALESCE logic), standardize temporal data, and ensure financial integrity.
3.  **Exploratory Data Analysis (EDA):** Multidimensional analysis focusing on seasonal trends, regional performance, and discount elasticity.
4.  **Strategic Recommendations:** Business-oriented insights aimed at margin optimization and inventory efficiency.

## 📈 Key Insights
* **Discount Inelasticity:** Analysis proved that high discounts (20%+) do not drive higher quantity per transaction, suggesting a pivot to volume-based bundles.
* **Hero Products:** Identified "White" color staples in Accessories and Dresses as the primary revenue drivers across all regions.
* **Seasonality Gap:** Detected a misalignment between product season attributes and actual sales months, leading to a recommendation for synchronized clearance windows.

## 📊 Visual Analysis Results

### Seasonal Sales Analysis
Analysis of transaction volume by month and product season:
![Seasonal Analysis](https://github.com/JesusAHB25/Lumina-Fashion-Group-End-to-End-Retail-Analytics-Pipeline/blob/main/images/Sales%20Count%20per%20Month%20&%20Season.png?raw=true)

### Category vs Color Heatmap
Identification of "Hero Products" through attribute correlation:
![Category Color Heatmap](https://github.com/JesusAHB25/Lumina-Fashion-Group-End-to-End-Retail-Analytics-Pipeline/blob/main/images/Sales%20Count%20by%20Category%20and%20Color.png?raw=true)

## 🚀 How to Run
1. Clone the repository: `git clone https://github.com/JesusAHB25/Lumina-Fashion-Group-End-to-End-Retail-Analytics-Pipeline.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Jupyter Notebook: `Lumina Fashion Group Analysis.ipynb`

## 📖 Documentation & Business Insights

While this repository contains the technical implementation, the complete business case, including deep-dive analysis and executive-level reporting, is documented in Notion.

### **Detailed Case Study**
You can access the full project walkthrough here: 

[![Notion](https://img.shields.io/badge/Notion-Full_Project_Report-black?style=for-the-badge&logo=notion)](https://purring-sailboat-492.notion.site/Jesus-Hernandez-Data-Portfolio-24d1d3119ed080c5bf0de65a37694de5?source=copy_link)

👉 **[Lumina Fashion Group - Full Strategic Report](https://purring-sailboat-492.notion.site/Lumina-Fashion-Group-Retail-Analytics-End-to-End-Pipeline-2b01d3119ed08066b5f9f147da60599c?source=copy_link)**

### **What’s inside the documentation?**

* **🏗️ Data Architecture:** Design of a **Star Schema** to unify 4 decoupled data domains into a single relational environment.
* **🧹 Cleaning Protocols:** Technical log of null imputation (1,000+ rows) and data standardization to ensure **Zero-Bias** results.
* **📈 EDA & Storytelling:** Advanced visualizations (Heatmaps & Time-Series) translating Python logic into executive business narratives.
* **🎯 Strategic Roadmap:** 4-pillar action plan for **margin optimization** and inventory realignment based on data-driven findings.

---
*Developed by Jesús with 🫐 and 🧮 - Data Analyst / Future Data Scientist*
