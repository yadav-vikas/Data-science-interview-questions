from pyspark.sql.functions import sequence, to_date, expr
from pyspark.sql.functions import to_date, month, year, date_format, col, explode
from pyspark.sql import SparkSession

# Create a Spark Session
spark = SparkSession.builder.appName("MySpark").getOrCreate()

# Create a DataFrame with start and end date of 2025
df = spark.createDataFrame([("2025-01-01", "2025-12-01")], ["start", "end"])

# Convert string to date
df = df.select(
    to_date("start").alias("start_date"),
    to_date("end").alias("end_date")
)

# Use expr to generate sequence with 1-month interval
df = df.select(
    expr("sequence(start_date, end_date, interval 1 month) as month_seq")
)

# Explode the sequence and format as yyyy-MM
df = df.select(
    explode("month_seq").alias("month_date")
).select(
    date_format("month_date", "yyyy-MM").alias("month")
)

df.show()

data_df = [
  ('T1','2025-01-10',100),
  ('T2','2025-01-15',200),
  ('T3','2025-03-05',300),
  ('T4','2025-05-20',400),
]

data_df_cols = ['txn_id','txn_date','amount']

data_df = spark.createDataFrame(data_df, data_df_cols)

data_df = data_df.withColumn('txn_date', date_format(to_date(col('txn_date')), "yyyy-MM"))

data_df.show()

df.join(data_df, df.month==data_df.txn_date, how='left_anti').orderBy('month').show()