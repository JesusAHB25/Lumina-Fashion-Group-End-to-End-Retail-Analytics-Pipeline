# IMPORTING DEPENDENCIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# LOADING DATA INTO DATAFRAMES
customer_data = pd.read_csv(r'C:\Users\MrJes\OneDrive\Data Analysis\End-To-End Projects\Lumina Fashion Group\.csv files\customer_data.csv')
product_data = pd.read_csv(r'C:\Users\MrJes\OneDrive\Data Analysis\End-To-End Projects\Lumina Fashion Group\.csv files\product_data.csv')
sales_data = pd.read_csv(r'C:\Users\MrJes\OneDrive\Data Analysis\End-To-End Projects\Lumina Fashion Group\.csv files\sales_data.csv')
store_data = pd.read_csv(r'C:\Users\MrJes\OneDrive\Data Analysis\End-To-End Projects\Lumina Fashion Group\.csv files\store_data.csv')

# DICTIONARY FOR THE UPCOMING LOOP
dataframes = {'customers' : customer_data,
              'products' : product_data,
              'sales' : sales_data,
              'stores' : store_data}

# LOOP TO AUTOMATE THE PROCESS
for name, file in dataframes.items():        
    print(f'[---] {name} SCHEMA INFO [---]')        
    print(f'\n{file.info()}') 
    print('[---] NULL VALUE COUNT [---]')
    print(f'\n{file.isnull().sum()}') 
    print('[---] DUPLICATE RECORD COUNT [---]')
    print(f'\n{file.duplicated().sum()}')

# CREATING POSTGRE SQL ENGINE
engine = create_engine('postgresql://postgres:J.e.s.u.s01*@localhost:5432/lumina_fashion_group')

for table_name, df in dataframes.items():
    df.to_sql(table_name, engine, if_exists='replace', index=False)

# CREATION OF THE MASTER QUERY FOR DATA SANITIZATION
master_query = """
SELECT 
    s.transaction_id,
    s.date::DATE, -- Standardization of date format
    COALESCE(s.customer_id, 'GUEST-001') as customer_id, -- Handling missing IDs
    p.season,
    st.store_name,
    st.region,
    p.product_id, -- Used as primary identifier
    REPLACE(p.category, '???', 'Other') as category, -- Handling missing categories
    COALESCE(p.color, 'Unspecified') as color, -- Handling missing colors
    p.size,
    s.quantity,
    p.list_price,
    COALESCE(s.discount, 0) as discount_pct, -- Treating null discounts as zero
    (s.quantity * p.list_price) * (1 - COALESCE(s.discount, 0)) as net_revenue -- Calculation of Net Revenue after discounts
FROM sales s
LEFT JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id
JOIN stores st ON s.store_id = st.store_id;
"""
master_df = pd.read_sql(master_query, engine)
