from pyspark.sql.functions import col, avg
from pyspark.sql import SparkSession

# Create a Spark Session
spark = SparkSession.builder.appName("MySpark").getOrCreate()



data1 = [
    ('2025-01-01','T1',100),
('2025-01-01','T2',200),
('2025-01-01','T3',500),
('2025-01-02','T4',300),
('2025-01-02','T5',400),
('2025-01-02','T6',600),
]

data_cols = ['txn_date', 'txn_id', 'amount']

data1_df = spark.createDataFrame(data1, data_cols)

data1_df.show()

data1_df_rs = data1_df.groupBy('txn_date').agg(avg('amount').alias('avg_amount'))

data1_df.join(data1_df_rs, on=['txn_date'], how='inner').filter(col('amount') > col('avg_amount')).select('txn_date', 'txn_id', 'amount').show()

data1_df.createOrReplaceTempView("user_txn")

data1_df_rs_sql = spark.sql("""
  with avg_txn as (
    select txn_date, avg(amount) as avg_amount from user_txn group by txn_date
  )
  select user_txn.txn_date, user_txn.txn_id, user_txn.amount from user_txn inner join avg_txn on user_txn.txn_date = avg_txn.txn_date where user_txn.amount > avg_txn.avg_amount

""")

data1_df_rs_sql.show()