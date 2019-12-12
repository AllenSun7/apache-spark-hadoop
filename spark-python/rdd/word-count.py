from pyspark import SparkContext, SparkConf
import pysnooper
import enchant
def get_palindrome():
    
    d = enchant.Dict("en_US")
    conf = SparkConf().setAppName("word count").setMaster("local[3]")
    sc = SparkContext(conf = conf)
    #df = sqlContext.parquetFile('/dir1/dir1_2', '/dir2/dir2_1')

    lines = sc.textFile("../maildir/*")
    #lines = sc.textFile("../test-data/*")
    
    words = lines.flatMap(lambda line: line.split(" "))
    
    wordCounts = words.countByValue()
    for word, count in wordCounts.items():
        if len(word) > 2: #if more than 2 letters
            if d.check(word): #if words
                if word == word[::-1]: #if palindrome
                    #ascii A-Z (65-90), a-z (97-122)
                    ascii_word = ord(word[0])
                    if 65 < ascii_word < 90 or 97 <ascii_word < 122:
                        print("{} : {}".format(word, count))


def main():
    get_palindrome()


if __name__ == "__main__":
    main()

