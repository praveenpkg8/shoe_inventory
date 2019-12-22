import os
import glob
import redis
import multiprocessing
from pyspark.sql import SparkSession

redis_store = redis.Redis(port=6379)


def populate_data(file_name):
    spark_sc = SparkSession.builder.appName("Populating data") \
        .config("spark.some.config.option", "pyspakr_config").getOrCreate()
    dataframe = spark_sc.read.csv(file_name, header=True, sep=',')

    return


def extract_file(path):
    update_path = "{}/*.csv".format(path)
    file_list = glob.glob(update_path)
    return file_list



def main():
    path = os.path.join(os.path.abspath('.'), 'womens-shoes-prices')
    file_list = extract_file(path)
    process = multiprocessing.Pool(len(file_list))
    process.map(populate_data, file_list)
    print(file_list)

if __name__ == '__main__':
    main()