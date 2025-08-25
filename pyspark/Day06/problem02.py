from pyspark.sql.functions import countDistinct

from pyspark.sql import SparkSession

# Create a Spark Session
spark = SparkSession.builder.appName("MySpark").getOrCreate()

data = [
    ('P1','2025-01-10'),
    ('P1','2025-02-12'),
    ('P1','2025-03-09'),
    ('P1','2025-04-18'),
    ('P1','2025-05-03'),
    ('P1','2025-06-27'),
    ('P1','2025-07-14'),
    ('P1','2025-08-21'),
    ('P1','2025-09-02'),
    ('P1','2025-10-11'),
    ('P1','2025-11-06'),
    ('P1','2025-12-05'),
    ('P2','2025-01-05'),
    ('P2','2025-02-10'),
    ('P2','2025-03-15'),
    ('P2','2025-05-20'),
    ('P2','2025-06-08'),
    ('P2','2025-07-22'),
    ('P2','2025-08-30'),
    ('P2','2025-10-01'),
    ('P2','2025-11-19'),
    ('P2','2025-12-07'),
    ('P3','2025-01-02'),
    ('P3','2025-02-14'),
    ('P3','2025-03-03'),
    ('P3','2025-04-25'),
    ('P3','2025-05-09'),
    ('P3','2025-06-16'),
    ('P3','2025-07-07'),
    ('P3','2025-08-12'),
    ('P3','2025-09-28'),
    ('P3','2025-10-20'),
    ('P3','2025-11-03'),
    ('P3','2025-12-29'),
]

cols = ['product_id', 'sale_date']


datadf = spark.createDataFrame(data, cols)

datadf.createOrReplaceTempView('month_sales')

datadf_sql = spark.sql("""

select  product_id, count(DISTINCT sale_date) as month_sale_count from month_sales group by product_id having month_sale_count >= 12

""")

datadf_sql.show()

datadf.groupBy('product_id').agg(countDistinct('sale_date').alias('month_sale_count')).filter(col('month_sale_count') >= 12).show()