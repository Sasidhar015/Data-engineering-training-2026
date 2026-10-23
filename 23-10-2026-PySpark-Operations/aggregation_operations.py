
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum, avg, min, max, countDistinct

spark = SparkSession.builder \
    .appName("aggregateoper") \
    .getOrCreate()

data = [
    (101, "Laptop", "Electronics", 65000),
    (102, "Mouse", "Accessories", 1500),
    (103, "Laptop", "Electronics", 65000),
    (104, "Keyboard", "Accessories", 3000),
    (105, "Mouse", "Accessories", 1500),
    (106, None, "Electronics", 18000),
    (107, "Monitor", None, 20000),
    (108, "Chair", "Furniture", None)]

columns = ["product_id", "product_name", "category", "price"]

df = spark.createDataFrame(data, columns)

print("Original DataFrame:")
df.show()


df.select(count("*").alias("total_rows")).show()


df.select(count("product_name").alias("product_name_count")).show()


df.select(sum("price").alias("total_price")).show()


df.select(avg("price").alias("average_price")).show()


df.select(min("price").alias("minimum_price")).show()


df.select(max("price").alias("maximum_price")).show()


df.select(countDistinct("product_name").alias("unique_product_names")).show()

df.groupBy("category").agg(count("*").alias("product_count")).show()

df.groupBy("category").agg( sum("price").alias("total_price")).show()

df.groupBy("category", "product_name").count().show()


df.agg(count("*").alias("total_rows"),
    sum("price").alias("total_price"),
    avg("price").alias("average_price"),
    min("price").alias("minimum_price"),
    max("price").alias("maximum_price")).show()

