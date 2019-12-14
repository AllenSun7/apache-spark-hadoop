from pyspark import SparkContext, SparkConf
import pysnooper
import enchant
import os
from collections import defaultdict
import timeit

def word_count():
    # count words of palindrome and anagram respectively
    conf = SparkConf().setAppName("Apache spark").setMaster("local[6]")
    sc = SparkContext(conf = conf)
    #lines = sc.textFile("in/maildir/*") #all dataset
    lines = sc.textFile("in/allen-p/*") # partial data
    #lines = sc.textFile("in/allen-p/_sent_mail/*") # partial data
    #lines = sc.textFile("in/test-data/*") # test data   

    words = lines.flatMap(lambda line: line.split(" "))  
    wordCounts = words.countByValue()
    d = enchant.Dict("en_US") #english word
    contents_anagram = list_anagram()
    dic_anagram = {}
    dic_palindrome = {"palindrome": "count"}
    for word, count in wordCounts.items():
        if len(word) > 2: #a work must contain more than 2 letters
            if d.check(word): #if it is a english word
                #ascii A-Z (65-90), a-z (97-122)
                ascii_word = ord(word[0])
                if ascii_word in range(65, 91) or ascii_word in range(97, 123):
                    word_dic = {word: count}
                    #check if it is a palindrome
                    if get_palindrome(word, count):
                        dic_palindrome.update(word_dic)
                    #check if it is a anagram
                    if get_anagram(word, count, contents_anagram):  
                        dic_anagram.update(word_dic)
                        
    print("================================================================")
    print("Palindrome") 
    print(dic_palindrome) 
    print("=============================")
    print("Anagram") 
    group_dic_anagram = group_anagram(dic_anagram)
    print(group_dic_anagram)
    print("================================================================")
    

def get_palindrome(word, count):
    #palindrome
    if word == word[::-1]:  
        #not same characters: "AAA","BBB"...
        if not all(c == word[0] for c in word[1:]):
            return True

def get_anagram(word, count, contents_anagram):
    #anagram
    if word in contents_anagram:
        return True

def list_anagram():
    #read the file of all anagrams and store into array
    #get absolute path
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'anagrams.txt')
    with open(my_file, "r") as ins:
        array = [line.strip() for line in ins]
    return array

def group_anagram(dic_anagram):
    # using defaultdict() + sorted() + values() 
    # Grouping Anagrams 
    test_list = [{key: value} for key, value in dic_anagram.items()]
    temp = defaultdict(list) 
    for ele in test_list: 
        for key in ele:
            temp[str(sorted(key))].append(ele) 
    res = list(temp.values())   
    return str(res)


def main():
    #cauculate runtime
    start = timeit.default_timer()
    word_count()
    stop = timeit.default_timer()
    print('Runtime: ', stop - start) 

if __name__ == "__main__":
    main()



