from pyspark import SparkContext, SparkConf
import pysnooper
import enchant

def word_count():

    
    conf = SparkConf().setAppName("Apache Apark").setMaster("local[6]")
    sc = SparkContext(conf = conf)

    #lines = sc.textFile("../maildir/*") #all dataset
    lines = sc.textFile("../allen-p/*")
    
    words = lines.flatMap(lambda line: line.split(" "))
    
    wordCounts = words.countByValue()
    d = enchant.Dict("en_US")
    for word, count in wordCounts.items():
        if len(word) > 2: #if more than 2 letters
            if d.check(word): #if it is a english word
                #ascii A-Z (65-90), a-z (97-122)
                ascii_word = ord(word[0])
                if 65 < ascii_word < 90 or 97 <ascii_word < 122:
                    get_palindrome(word, count)    


def get_palindrome(word, count):
    #palindrome
    if word == word[::-1]:  
        print("{} : {}".format(word, count))
    # not same letters "AAA\BBB"

def main():
    word_count()


if __name__ == "__main__":
    main()

