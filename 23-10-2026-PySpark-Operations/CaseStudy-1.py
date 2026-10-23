from pyspark.sql import SparkSession
from pyspark.sql.functions import col

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



df.orderBy(col("price").asc()).show()


df.orderBy(col("price").desc()).show()


df.orderBy(
    col("category").asc(),
    col("price").desc()
).show()


df1 = df.withColumn("gross_amount", col("price"))

df1.orderBy(
    col("gross_amount").desc()
).show(10)


df.orderBy(
    col("price").asc()
).show(5)

spark.stop()
