import sys
 
from pyspark import SparkContext, SparkConf
 
if __name__ == "__main__":
 
  # create Spark context with Spark configuration
  conf = SparkConf().setAppName("Read Text to RDD - Python")
  sc = SparkContext(conf=conf)
 
  # read input text files present in the directory to RDD
  lines = sc.textFile("in/maildir/*")
 
  # collect the RDD to a list
  llist = lines.collect()

  # print the list
  i = 1
  for line in llist:
    print(i)
    i += 1