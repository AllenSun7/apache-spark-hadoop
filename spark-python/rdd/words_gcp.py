"""
for subdirectionary only
read all files at the same time
"""

from pyspark import SparkContext, SparkConf
import pysnooper
import os
from collections import defaultdict
import timeit
import pysnooper
import json
from glob import glob
import os
import json

def word_count():
    '''count words of palindrome and anagram respectively'''
    conf = SparkConf().setAppName("Apache spark").setMaster("local[5]") # 4 cores [*] all available cores
    sc = SparkContext(conf = conf)

    parent_path = "gs://apache-dataset-all/test-data/*"

    lines = sc.textFile(parent_path) 
    init_words = lines.flatMap(lambda line: line.split(" "))  
    words = init_words.filter(lenth_words)
    wordCounts = words.countByValue()
    dic_palindrome, dic_anagram = words_filter(wordCounts)
      

    print("================================================================")    
    print("Palindrome") 
    print(dic_palindrome) 
    print("=============================")
    print("Anagram") 
    group_dic_anagram = group_anagram(dic_anagram)
    print(group_dic_anagram)
    print("================================================================")

    #json file
    with open('out/invalid/spark-palindrome/' + filename + '.json', 'w') as outfile:
        json.dump(dic_palindrome, outfile)
    with open('out/invalid/spark-anagram/' + filename + '.json', 'w') as outfile:
        json.dump(dic_anagram, outfile)

def lenth_words(word):
    return (len(word) in range(2, 20))

def words_filter(wordCounts):
    '''filter words'''
    contents_anagram = list_anagram()
    dic_anagram = {}
    dic_palindrome = {}
    for word, count in wordCounts.items():
        if len(word) > 2: #a work must contain more than 2 letters
            #letters only: ascii A-Z (65-90), a-z (97-122)
            ascii_word = ord(word[0])
            if ascii_word in range(65, 91) or ascii_word in range(97, 123):
                word_dic = {word: count}
                #check if it is a palindrome
                if get_palindrome(word):
                    dic_palindrome.update(word_dic)
                #check if it is a anagram
                if get_anagram(word, contents_anagram):  
                    dic_anagram.update(word_dic)
                        
    return (dic_palindrome, dic_anagram)

def get_palindrome(word):
    '''palindrome'''
    #not same characters: "AAA","BBB"...
    return (word == word[::-1] and not all(c == word[0] for c in word[1:]))

def get_anagram(word, contents_anagram):
    '''anagram'''
    return (word in contents_anagram)

def list_anagram():
    '''read the input file of all anagrams and store into array'''
    #get absolute path
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'anagrams.txt')
    with open(my_file, "r") as ins:
        array = [line.strip() for line in ins]
    return array

def group_anagram(dic_anagram):
    '''Grouping Anagrams by using defaultdict() + sorted() + values()'''   
    test_list = [{key: value} for key, value in dic_anagram.items()]
    temp = defaultdict(list) 
    for ele in test_list: 
        for key in ele:
            temp[str(sorted(key))].append(ele) 
    res = list(temp.values())   
    return res

def main():
    '''cauculate runtime'''
    start = timeit.default_timer()
    word_count()
    stop = timeit.default_timer()
    time = stop - start
    print('Runtime: ', time)  

if __name__ == "__main__":
    main()



