from pyspark.sql import SparkSession

from pyspark.sql.functions import col
from pyspark.sql import Window
from pyspark.sql.functions import rank

# Create a Spark Session
spark = SparkSession.builder.appName("MySpark").getOrCreate

data1= [
    (101,'2025-01-03',250),
    (101,'2025-01-05',300),
    (102,'2025-01-01',150),
    (102,'2025-01-02',200),
    (103,'2025-01-04',500),
]

cols = ['customer_id', 'purchase_date', 'amount']


data1_df = spark.createDataFrame(data1, cols)

data1_df.show()

data1_df_win = Window.partitionBy('customer_id').orderBy('purchase_date')
data1_df = data1_df.withColumn('rank', rank().over(data1_df_win))
data1_df.filter(col('rank')==1).select('customer_id', 'purchase_date', 'amount').show()

data1_df.createOrReplaceTempView("user_purchase")


data1_df_sql = spark.sql("""
  with temp_sales as (select customer_id, purchase_date, amount, rank() over(partition by customer_id order by purchase_date asc) as order_rank from user_purchase)
  select customer_id, purchase_date, amount from temp_sales where order_rank=1

""")

data1_df_sql.show()