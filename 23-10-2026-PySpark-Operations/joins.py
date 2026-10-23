# INNER JOIN

orders.join(customers,
    on="customer_id",
    how="inner").select(
    "order_id", "customer_id", "customer_name", "city",
    "product_id", "quantity", "unit_price", "status").show(10, truncate=False)



# LEFT JOIN

orders.join(customers,
    on="customer_id",
    how="left").select(
    "order_id", "customer_id", "customer_name", "city", "status").show(10, truncate=False)



# RIGHT JOIN 

orders.join(customers,
    on="customer_id",
    how="right").select(
    "order_id", "customer_id", "customer_name", "city", "region").show(10, truncate=False)


# OUTTER JOIN 

orders.join(customers,
    on="customer_id",
    how="full_outer").select(
    "order_id", "customer_id", "customer_name", "city").show(10, truncate=False)
