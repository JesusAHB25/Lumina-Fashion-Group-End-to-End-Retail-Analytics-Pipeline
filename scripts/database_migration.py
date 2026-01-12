import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# --- DIRECTLY EXTRACTED FROM MY NOTEBOOK ---

# From Cell 172: Loading datasets
customer_data = pd.read_csv(r'C:\Users\MrJes\OneDrive\Data Analysis\End-To-End-Retail-Analytics-Pipeline\data\customer_data.csv')
product_data = pd.read_csv(r'C:\Users\MrJes\OneDrive\Data Analysis\End-To-End-Retail-Analytics-Pipeline\data\product_data.csv')
sales_data = pd.read_csv(r'C:\Users\MrJes\OneDrive\Data Analysis\End-To-End-Retail-Analytics-Pipeline\data\sales_data.csv')
store_data = pd.read_csv(r'C:\Users\MrJes\OneDrive\Data Analysis\End-To-End-Retail-Analytics-Pipeline\data\store_data.csv')

# From Cell 175: Connection setup
engine = create_engine('postgresql://postgres:J.e.s.u.s01*@localhost:5432/lumina_fashion_group')

# From Cell 181: Migration logic
dataframes = {
    'customers': customer_data,
    'products': product_data,
    'sales': sales_data,
    'stores': store_data
}

for table_name, df in dataframes.items():
    df.to_sql(table_name, engine, if_exists='replace', index=False)
