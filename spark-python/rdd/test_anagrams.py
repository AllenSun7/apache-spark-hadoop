from pyspark import SparkContext, SparkConf
import pysnooper
import enchant
import os

def word_count():
    # count words of palindrome and anagram respectively
    conf = SparkConf().setAppName("Apache spark").setMaster("local[6]")
    sc = SparkContext(conf = conf)
    #lines = sc.textFile("in/maildir/*") #all dataset
    lines = sc.textFile("in/allen-p/*") # partial data
    #lines = sc.textFile("in/test-data/*") # test data   
    words = lines.flatMap(lambda line: line.split(" "))  
    wordCounts = words.countByValue()
    d = enchant.Dict("en_US") #english word
    contents_anagram = list_anagram()
    for word, count in wordCounts.items():
        if len(word) > 2: #a work must contain more than 2 letters
            if d.check(word): #if it is a english word
                #ascii A-Z (65-90), a-z (97-122)
                ascii_word = ord(word[0])
                if 65 <= ascii_word <= 90 or 97 <= ascii_word <= 122:
                    #get_palindrome(word, count)  
                    get_anagram(word, count, contents_anagram)  


def get_palindrome(word, count):
    #palindrome
    if word == word[::-1]:  
        #not same characters: "AAA","BBB"...
        if not all(c == word[0] for c in word[1:]): 
            print("{} : {}".format(word, count))

def get_anagram(word, count, contents_anagram):
    #anagram
    if word in contents_anagram:
        print("{} : {}".format(word, count))

def list_anagram():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'anagrams.txt')
    f=open(my_file, "r")
    #f=open("../in/anagrams.txt", "r")
    contents =f.read()
    f.close()
    return contents

def main():
    word_count()

if __name__ == "__main__":
    main()



