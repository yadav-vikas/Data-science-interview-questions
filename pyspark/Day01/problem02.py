from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DateType

# Create a Spark Session
spark = SparkSession.builder.appName("MySpark").getOrCreate()

# Prepare the data as a list of rows
data = [
    (1, "2025-01-01"),
    (1, "2025-01-02"),
    (1, "2025-01-04"),
    (2, "2025-01-01"),
    (2, "2025-01-02"),
    (2, "2025-01-03"),
    (2, "2025-01-05")
]

# Convert the data to a DataFrame
user_login_df = spark.createDataFrame(data, ['user_id','login_date'])

user_login_df = user_login_df.withColumn('login_date', (col('login_date').cast('date')))

# Display the DataFrame
user_login_df.show()

# find difference between the dates using lag window function
win_df = Window.partitionBy('user_id').orderBy('login_date')
user_df = user_login_df.withColumn('next_date', lag('login_date').over(win_df))

# calculate the count of rows with diff=1 as streak count
user_df = user_df.withColumn('diff', datediff(col('next_date'), col('login_date')))
result = user_df.groupBy('user_id').agg(count('diff').alias('streak'))
result.show()