from pyspark.sql import SparkSession

from pyspark.sql import Window
from pyspark.sql.functions import col, lit, ntile

# Create a Spark Session
spark = SparkSession.builder.appName("MySpark").getOrCreate()

data = [
    ('Electronics','Laptop',1200),
    ('Electronics','Phone',900),
    ('Electronics','Tablet',700),
    ('Clothing','Shirt',400),
    ('Clothing','Jeans',600),
    ('Clothing','Jacket',800)
]

cols = ['category','product','sales']

d2df = spark.createDataFrame(data, cols)

d2df.show()

win_datadf = Window.partitionBy('category').orderBy(col('sales').desc())
datadf = d2df.withColumn('rnk', ntile(2).over(win_datadf))
datadf.filter(col('rnk')==1).select('category', 'product', 'sales').orderBy(col('sales').desc()).show()

################### SQL Soluton ###################
d2df.createOrReplaceTempView("user_sales_table")

d2df_result = spark.sql("""
  with temp_sales as (
    select category, product, sales, NTILE(2) over(partition by category order by sales desc) as rnk from user_sales_table
  )
  select category, product, sales from temp_sales where rnk=1 order by sales desc

""")

d2df_result.show()