from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RetailTransactionsAssessment").getOrCreate()

CSV_PATH = "retail_transactions_100k.csv"

df = (spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(CSV_PATH))

print("Total records:", df.count())  
df.show(5, truncate=False)
df.printSchema()


# 1. Display the first 20 records.
df.show(20, truncate=False)

# 2. Display the schema.
df.printSchema()

# 3. Display all column names.
print(df.columns)

# 4. Count the total number of records.
print("Total records:", df.count())

# 5. Display selected columns.
df.select("order_id", "product_name", "city", "quantity", "unit_price").show()

# 6. Display Electronics transactions.
df.filter(col("category") == "Electronics").show()

# 7. Display transactions from Hyderabad.
df.filter(col("city") == "Hyderabad").show()

# 8. Display transactions where quantity is greater than 3.
df.filter(col("quantity") > 3).show()

# 9. Display transactions where unit price is greater than ₹20,000.
df.filter(col("unit_price") > 20000).show()

# 10. Display Delivered transactions.
df.filter(col("status") == "Delivered").show()

# 11. Electronics transactions from Hyderabad.
df.filter((col("category") == "Electronics") & (col("city") == "Hyderabad")).show()

# 12. Delivered transactions from the South region.
df.filter((col("status") == "Delivered") & (col("region") == "South")).show()

# 13. Quantity > 2 and unit price > ₹10,000.
df.filter((col("quantity") > 2) & (col("unit_price") > 10000)).show()

# 14. Transactions from either Mumbai or Pune.
df.filter(col("city").isin("Mumbai", "Pune")).show()

# 15. Transactions that are not Cancelled.
df.filter(col("status") != "Cancelled").show()

# 16. Furniture products costing more than ₹8,000.
df.filter((col("category") == "Furniture") & (col("unit_price") > 8000)).show()

# 17. Accessories products with quantity greater than 3.
df.filter((col("category") == "Accessories") & (col("quantity") > 3)).show()

# 18. Select order_id, customer_name, product_name, unit_price.
df.select("order_id", "customer_name", "product_name", "unit_price").show()

# 19. Rename unit_price to price.
df.withColumnRenamed("unit_price", "price").show(5)

# 20. Rename customer_name to customer.
df.withColumnRenamed("customer_name", "customer").show(5)

# 21. Drop the rating column.
df.drop("rating").show(5)

# 22. Drop customer_name, rating, and payment_method from a new DataFrame.
df_without_details = df.drop("customer_name", "rating", "payment_method")
df_without_details.show(5)

# 23. gross_amount = quantity * unit_price.
df = df.withColumn("gross_amount", col("quantity") * col("unit_price"))

# 24. discount_amount = gross_amount * discount_pct / 100.
df = df.withColumn("discount_amount",
    col("gross_amount") * col("discount_pct") / 100)

# 25. final_amount = gross_amount - discount_amount.
df = df.withColumn("final_amount",
    col("gross_amount") - col("discount_amount"))

# 26. Add a constant column: country = India.
df = df.withColumn("country", lit("India"))

# 27. high_value: final_amount >= 50000 => Yes, otherwise No.
df = df.withColumn("high_value",
    when(col("final_amount") >= 50000, lit("Yes")).otherwise(lit("No")))
df.select("order_id", "gross_amount", "discount_amount",
    "final_amount", "country", "high_value").show(10)

# 28. order_size: High / Medium / Low.
df = df.withColumn(
    "order_size",
    when(col("final_amount") >= 50000, "High")
    .when(col("final_amount") >= 15000, "Medium")
    .otherwise("Low"))

# 29. quantity_type: quantity >= 4 => Bulk, otherwise Regular.
df = df.withColumn(
    "quantity_type",
    when(col("quantity") >= 4, "Bulk").otherwise("Regular"))

# 30. Delivery-status category.
df = df.withColumn(
    "delivery_status_category",
    when(col("status") == "Delivered", "Completed")
    .when(col("status").isin("Cancelled", "Returned"), "Failed")
    .otherwise("In Progress"))
df.select("order_id", "status", "order_size",
    "quantity_type", "delivery_status_category").show(10)

# 31. Sort by unit price, highest to lowest.
df.orderBy(col("unit_price").desc()).show()

# 32. Sort by quantity, highest to lowest.
df.orderBy(col("quantity").desc()).show()

# 33. Sort alphabetically by city.
df.orderBy(col("city").asc()).show()

# 34. Sort by region ascending, then final amount descending.
df.orderBy(col("region").asc(), col("final_amount").desc()).show()

# 35. Display the 10 highest-value transactions.
df.orderBy(col("final_amount").desc()).show(10, truncate=False)

# 36. Display unique cities.
df.select("city").distinct().orderBy("city").show()

# 37. Display unique regions.
df.select("region").distinct().orderBy("region").show()

# 38. Display unique product categories.
df.select("category").distinct().orderBy("category").show()

# 39. Display unique payment methods.
df.select("payment_method").distinct().orderBy("payment_method").show()

# 40. Count unique customers.
print("Unique customers:", df.select("customer_id").distinct().count())

# 41. Count unique products.
print("Unique products:", df.select("product_id").distinct().count())

# 42. Total quantity sold.
df.select(sum("quantity").alias("total_quantity_sold")).show()

# 43. Total gross sales.
df.select(sum("gross_amount").alias("total_gross_sales")).show()

# 44. Average unit price.
df.select(avg("unit_price").alias("average_unit_price")).show()

# 45. Maximum unit price.
df.select(max("unit_price").alias("maximum_unit_price")).show()

# 46. Minimum unit price.
df.select(min("unit_price").alias("minimum_unit_price")).show()

# 47. Total discount given.
df.select(sum("discount_amount").alias("total_discount_given")).show()

# 48. Total final sales value.
df.select(sum("final_amount").alias("total_final_sales")).show()

# 49. Count transactions by status.
df.groupBy("status").count().orderBy(col("count").desc()).show()

# 50. Count transactions by category.
df.groupBy("category").count().orderBy(col("count").desc()).show()

# 51. Count transactions by city.
df.groupBy("city").count().orderBy(col("count").desc()).show()

# 52. Total sales by region.
df.groupBy("region").agg(sum("final_amount").alias("total_sales")) \.orderBy(col("total_sales").desc()).show()

# 53. Total sales by category.
df.groupBy("category").agg(sum("final_amount").alias("total_sales")) \.orderBy(col("total_sales").desc()).show()

# 54. Average unit price by category.
df.groupBy("category").agg(avg("unit_price").alias("average_unit_price")) \.orderBy(col("average_unit_price").desc()).show()

# 55. Total quantity sold by product.
df.groupBy("product_name").agg(sum("quantity").alias("total_quantity")) \.orderBy(col("total_quantity").desc()).show()

# 56. Total sales by payment method.
df.groupBy("payment_method").agg(sum("final_amount").alias("total_sales")) \.orderBy(col("total_sales").desc()).show()

# 57. Average rating by product.
df.groupBy("product_name").agg(avg("rating").alias("average_rating")) \.orderBy(col("average_rating").desc()).show()

# 58. Total orders by city and status.
df.groupBy("city", "status").count().orderBy("city", "status").show()

# 59. Total sales by city, highest to lowest.
df.groupBy("city").agg(sum("final_amount").alias("total_sales")) \.orderBy(col("total_sales").desc()).show()

# 60. Total quantity sold by product, highest to lowest.
df.groupBy("product_name").agg(sum("quantity").alias("total_quantity")) \.orderBy(col("total_quantity").desc()).show()

# 61. Category-wise average unit price, descending.
df.groupBy("category").agg(avg("unit_price").alias("average_unit_price")) \.orderBy(col("average_unit_price").desc()).show()

# 62. Top 5 cities based on total sales.
df.groupBy("city").agg(sum("final_amount").alias("total_sales")) \.orderBy(col("total_sales").desc()).show(5)

# 63. Top 5 products based on quantity sold.
df.groupBy("product_name").agg(sum("quantity").alias("total_quantity")) \.orderBy(col("total_quantity").desc()).show(5)

# 64. Top 10 customers based on purchase amount.
df.groupBy("customer_id", "customer_name") \
    .agg(sum("final_amount").alias("purchase_amount")) \
    .orderBy(col("purchase_amount").desc()).show(10, truncate=False)


df = df.withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))

# 65. Extract year.
df = df.withColumn("year", year(col("order_date")))

# 66. Extract month.
df = df.withColumn("month", month(col("order_date")))

# 67. Extract day.
df = df.withColumn("day", dayofmonth(col("order_date")))
df.select("order_date", "year", "month", "day").show(10)

# 68. Number of transactions by month.
df.groupBy("year", "month").count().orderBy("year", "month").show()

# 69. Total sales by month.
df.groupBy("year", "month").agg(sum("final_amount").alias("total_sales")) \.orderBy("year", "month").show()

# 70. Monthly sales by category.
df.groupBy("year", "month", "category") \.agg(sum("final_amount").alias("total_sales")) \.orderBy("year", "month", "category").show()

# 71. Monthly count by status.
df.groupBy("year", "month", "status").count() \ .orderBy("year", "month", "status").show()

# 72. Month having the highest sales.
df.groupBy("year", "month").agg(sum("final_amount").alias("total_sales")) \.orderBy(col("total_sales").desc()).show(1)

# 73. Find records where payment_method is missing.
df.filter(col("payment_method").isNull()).show()

# 74. Count missing payment methods.
print("Missing payment methods:",df.filter(col("payment_method").isNull()).count())

# 75. Find records where rating is missing.
df.filter(col("rating").isNull()).show()

# 76. Count missing ratings.
print("Missing ratings:", df.filter(col("rating").isNull()).count())

# 77. Replace missing payment methods with Unknown.
df_filled = df.fillna({"payment_method": "Unknown"})

# 78. Replace missing ratings with 0.
df_filled = df_filled.fillna({"rating": 0})

# 79. Drop records having missing payment methods.
df_without_missing_payment = df.filter(col("payment_method").isNotNull())
print("Records after dropping missing payment methods:",df_without_missing_payment.count())


