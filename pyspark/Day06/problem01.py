
from pyspark.sql import Window
from pyspark.sql.functions import col, rank
from pyspark.sql import SparkSession

# Create a Spark Session
spark = SparkSession.builder.appName("MySpark").getOrCreate()

data = [
  (1,'HR',60000),
  (2,'HR',75000),
  (3,'HR',50000),
  (4,'IT',90000),
  (5,'IT',85000),
]

cols = ['emp_id','dept','salary']

datadf = spark.createDataFrame(data, cols)

datadf.show()

data_win = Window.partitionBy('dept').orderBy(col('salary').desc())

datadf = datadf.withColumn('rank', rank().over(data_win))

datadf.show()

datadf.createOrReplaceTempView("user_dept")

datadf_sql = spark.sql("""
  with temp_dept as (
    select emp_id, dept, salary, rank() over(partition by dept order by salary desc) as rnk from user_dept
  )
  select emp_id, dept, salary, rnk from temp_dept

  """)

datadf_sql.show()