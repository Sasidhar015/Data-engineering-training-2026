from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DataCleaning") \
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

df.show()


df.sort(col("unit_price").asc()).show(10)

df.orderBy(col("city").asc()).show(10)

df.orderBy(col("unit_price").desc()).show(10)

df.orderBy(col("region").asc(), col("unit_price").asc()).show(10)

df.orderBy(col("unit_price").desc()).show(10, truncate=False)
