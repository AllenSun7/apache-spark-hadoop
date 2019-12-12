from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("word count").setMaster("local[3]")
    sc = SparkContext(conf = conf)
    #df = sqlContext.parquetFile('/dir1/dir1_2', '/dir2/dir2_1')

    lines = sc.textFile("../allen-p/_sent_mail/1.")
    
    words = lines.flatMap(lambda line: line.split(" "))
    
    wordCounts = words.countByValue()
    
    for word, count in wordCounts.items():
        if word == word[::-1]:
            print("True!!")
        print("{} : {}".format(word, count))

