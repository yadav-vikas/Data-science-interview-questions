from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.sql.functions import col, sum

# Create a Spark Session
spark = SparkSession.builder.appName("MySpark").getOrCreate

data2 = [
    (1,'2025-01-01',	500),
    (1,'2025-01-03',	-200),
    (1,'2025-01-05',	300),
    (2,'2025-01-02',	1000),
    (2,'2025-01-04',	-400),
]

cls = ['user_id',	'txn_date',	'amount']

data2df = spark.createDataFrame(data2, cls)
data2df = data2df.withColumn('txn_date', col('txn_date').cast('date'))
data2df.show()



win_df = Window.partitionBy('user_id').orderBy('txn_date').rowsBetween(Window.unboundedPreceding,0)

data2df = data2df.withColumn("transaction_data", sum('amount').over(win_df))

data2df.show()

################### SQL Soluton ###################
data2df.createOrReplaceTempView("user_txn_table")

data2df_result = spark.sql("""

select user_id, txn_date, amount, sum(amount) over(partition by user_id order by txn_date rows between unbounded preceding and current row) as transaction_data from user_txn_table

""")

data2df_result.show()