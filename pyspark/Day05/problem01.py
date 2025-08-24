from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, round, col, lit, expr

# Create a Spark Session
spark = SparkSession.builder.appName("MySpark").getOrCreate()

data_df = [
  ('Laptop',1200),
  ('Phone',800),
  ('Tablet',500),
  ('Desktop',500)
]
data_df_cols = ['product', 'sales']

data_df = spark.createDataFrame(data_df, data_df_cols)

data_df.show()

total_sales = data_df.agg(sum("sales").alias("total_sales")).collect()[0]["total_sales"]

data_df = data_df.withColumn(
    "percentage_contribution",
    round((col("sales") / total_sales) * 100, 1)
)

data_df.show()

data_df.createOrReplaceTempView("user_sales")

data_df_sql = spark.sql("""
    with total_sales as (
      select sum(sales) as total_sales from user_sales
    )
    select product, sales, round(sales*100/total_sales,2) as percentage from user_sales, total_sales

""")

data_df_sql.show()
