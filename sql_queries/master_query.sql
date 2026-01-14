SELECT 
    s.transaction_id,
    s.date::DATE, 
    COALESCE(s.customer_id, 'GUEST-001') as customer_id, 
    p.season,
    st.store_name,
    st.region,
    REPLACE(p.category, '???', 'Other') as category, 
    COALESCE(p.color, 'Unspecified') as color, 
    s.quantity,
    p.list_price,
    COALESCE(s.discount, 0) as discount_pct, 
    (s.quantity * p.list_price) * (1 - COALESCE(s.discount, 0)) as net_revenue 
FROM sales s
LEFT JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id
JOIN stores st ON s.store_id = st.store_id;
