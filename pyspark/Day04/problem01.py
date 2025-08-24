from pyspark.sql.functions import count, countDistinct
from pyspark.sql import SparkSession

# Create a Spark Session
spark = SparkSession.builder.appName("MySpark").getOrCreate()


data2 = [
  (1,10,'2025-01-01'),
  (1,10,'2025-02-01'),
  (2,11,'2025-01-01'),
  (2,12,'2025-03-01'),
  (3,13,'2025-01-05'),
]

data2_cols = ['emp_id', 'manager_id', 'change_date']

data2_df = spark.createDataFrame(data2, data2_cols)

data2_df.show()

data2_df_rs = data2_df.groupBy('emp_id').agg(countDistinct('manager_id').alias('cnt'))
data2_df_rs = data2_df_rs.filter(col('cnt') <= 1)
data2_df_rs.show()

data2_df_sql = data2_df.createOrReplaceTempView("user_emp")

data2_df_sql_rs = spark.sql("""

  select emp_id, count(DISTINCT manager_id) as cnt from user_emp group by emp_id having cnt <= 1

""")

data2_df_sql_rs.show()
