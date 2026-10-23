from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum, avg, min, max

spark = SparkSession.builder \
    .appName("GroupByPractice") \
    .getOrCreate()

data = [
    (101, "Laptop", "Electronics", 65000),
    (102, "Mouse", "Accessories", 1500),
    (103, "Laptop", "Electronics", 65000),
    (104, "Keyboard", "Accessories", 3000),
    (105, "Mouse", "Accessories", 1500),
    (106, None, "Electronics", 18000),
    (107, "Monitor", None, 20000),
    (108, "Chair", "Furniture", None)
]

columns = ["product_id", "product_name", "category", "price"]
df = spark.createDataFrame(data, columns)

print("Original DataFrame:")
df.show()


df.groupBy("category").count().show()


df.groupBy("product_name").count().show()


df.groupBy("category", "product_name").count().show()


df.groupBy("category").agg(sum("price").alias("total_price")).show()


df.groupBy("category").agg(avg("price").alias("average_price")).show()


df.groupBy("category").agg(min("price").alias("minimum_price")).show()


df.groupBy("category").agg(max("price").alias("maximum_price")).show()


df.groupBy("category").agg(
    count("*").alias("record_count"),
    sum("price").alias("total_price")).show()


df.groupBy("category").agg(
    count("*").alias("record_count"),
    sum("price").alias("total_price"),
    avg("price").alias("average_price"),
    min("price").alias("minimum_price"),
    max("price").alias("maximum_price")).show()



df.groupBy("category", "product_name").agg(sum("price").alias("total_price")).show()


df.groupBy("category", "product_name").agg(count("*").alias("record_count"),avg("price").alias("average_price")).show()
