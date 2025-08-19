from pyspark.sql import SparkSession
from pyspark.sql.functions import col, min, max, sequence, to_date

# Initialize a Spark Session
spark = SparkSession.builder.appName("MySpark").getOrCreate()

# Create the sample DataFrame
data = [("2025-01-01", 100), ("2025-01-02", 150), ("2025-01-04", 120), ("2025-01-06", 200)]
sales = spark.createDataFrame(data, ["date", "sales"])

# Cast the date column to a DateType
sales = sales.withColumn("date", to_date(col("date")))

# Find the minimum and maximum dates
min_date, max_date = sales.agg(min("date"), max("date")).first()

# Generate a sequence of all dates within the range
full_date_df = spark.createDataFrame([(min_date, max_date)], ["start", "end"]) \
    .withColumn("date", sequence(col("start"), col("end"))) \
    .selectExpr("explode(date) as date")

# Perform a left_anti join to find missing dates
missing_dates_df = full_date_df.join(sales, on="date", how="left_anti") \
    .select(col("date").alias("missing_date"))

# Display the result
missing_dates_df.show()