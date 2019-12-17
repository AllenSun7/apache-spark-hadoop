from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("word count").setMaster("local[3]")
    sc = SparkContext(conf = conf)
    
    lines = sc.textFile("in/maildir/*/*/*/*")
    
    words = lines.flatMap(lambda line: line.split(" "))
    
    wordCounts = words.countByValue()
    
    for word, count in wordCounts.items():
        if word == word[::-1]:
            print("True")
        print("{} : {}".format(word, count))