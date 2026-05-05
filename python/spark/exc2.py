# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: 
# AI2 InfinityLabs.
# ----------------------------
import pyspark


def main():
    spark = pyspark.sql.SparkSession.builder.appName("pysaprk_python").getOrCreate()
    df = spark.read.csv("banking.csv")
    print(df)


if __name__ == '__main__':
    main()
