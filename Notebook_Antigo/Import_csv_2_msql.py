from pyspark import SparkContext
sc = SparkContext()

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', sep=",", inferschema='true', encoding = 'ISO-8859-1').load(r'C:\Users\Ricardo\Downloads\MicrodadosEnem\MICRODADOS_ENEM_2015.csv')

df.write.format('jdbc').options(
    url='jdbc:mysql://localhost/enemdb?useTimezone=true&serverTimezone=UTC',
    driver='com.mysql.jdbc.Driver',
    dbtable='dados_2015',
    user='root', password='admin').mode('overwrite').save()
