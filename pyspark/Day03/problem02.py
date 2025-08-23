from pyspark.sql import SparkSession
from pyspark.sql.functions import count, col

# Create a Spark Session
spark = SparkSession.builder.appName("MySpark").getOrCreate

prb_data = [
    (1,'2025-01-01',50000),
    (1,'2025-02-01',55000),
    (1,'2025-03-01',60000),
    (2,'2025-01-15',40000),
    (2,'2025-03-01',45000),
    (3,'2025-01-10',30000),
]

cols = ['emp_id', 'effective_date', 'salary']

prb_df = spark.createDataFrame(prb_data, cols)

prb_df.show()

prb_df_result = prb_df.groupBy('emp_id').agg((count('*')-1).alias('salary_change_count')).filter(col('salary_change_count')>=1)

prb_df_result.show()

prb_df.createOrReplaceTempView("user_salary")

prb_result = spark.sql("""
  select emp_id, count(*)-1 as salary_change_count from user_salary group by emp_id having salary_change_count >= 1

""")

prb_result.show()