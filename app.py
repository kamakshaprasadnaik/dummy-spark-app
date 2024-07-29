from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window
from DataframeGenerator import DataGenerator
import random

#create spark session and dataframe
min_rows=50
max_rows=100
cols=['id', 'name', 'city', 'salary']
spark=SparkSession.builder.appName('CitySalaryAnalyser').getOrCreate()
spark.sparkContext.setLogLevel('ERROR')
data = DataGenerator(random.randint(min_rows, max_rows)).get_data()
print('Source Data Frame')
df=spark.createDataFrame(data, cols)
df.show()

#calculate the average salary for each city
#group by should be avoided as works on one key at a time takes huge toll on memory but for small dataset it's okay - kpn
print("City wise average salary")
df_avg_slry=df.groupby(df.city).agg(round(avg(df.salary),2).alias('average_salary')).orderBy(desc(col('average_salary')))
df_avg_slry.show(max_rows) #so that it shows all rows 

#rank people based on salaries
print("Rank of people based on salaries")
windowSpec=Window.orderBy(desc(col('salary')))
df_salary_rank=df.withColumn('salary_rank', dense_rank().over(windowSpec))
df_salary_rank.show(max_rows)

#check if there are people with same name in different cities
print("People with same name in multiple cities")
df_count=df.select(df.name, df.city).distinct().groupby(df.name).agg(count(df.city).alias('city_count')).filter(col('city_count')>1).orderBy(col('city_count'))
df_count.show(max_rows)

#richest person of each city
print("Richest person of each city")
max_slry_lkp=df.groupby(df.city).agg(max(df.salary).alias('max_salary'))
df_richest=df.join(max_slry_lkp, ((df.city==max_slry_lkp.city) & (df.salary==max_slry_lkp.max_salary)), 'inner').drop(max_slry_lkp.city, max_slry_lkp.max_salary).orderBy(desc(col('salary')))
df_richest.show(max_rows)

#who are getting salaries above average salary
print("People with salaries higher than average salary")
average_salary=df.select(avg(df.salary)).collect()[0][0]
df_grt_avg_salary=df.filter(df.salary>average_salary).orderBy(desc(df.salary))
df_grt_avg_salary.show(max_rows)

