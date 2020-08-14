from pyspark import SparkContext
sc = SparkContext()

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', sep=",", inferschema='true', encoding = 'ISO-8859-1', nrows=1000).load('C:/Users/pc/Downloads/MICRODADOS/MICRODADOS_ENEM_2015.csv')

#import sqlalchemy

#engine = sqlalchemy.create_engine('mysql+pymysql://root:admin@localhost/enemdb')

#df_pandas = df.select('*').toPandas()

#df_pandas.to_sql(
#    name = 'dados_2015',
#    con = engine,
#   index = False,
#    chunksize = 10000,
#    if_exists = 'replace'
#)

df.write.format('jdbc').options(
    url='jdbc:mysql://localhost/enemdb?useTimezone=true&serverTimezone=UTC',
    driver='com.mysql.jdbc.Driver',
    dbtable='dados_2015',
    user='root',
    password='admin').mode('append').save();
