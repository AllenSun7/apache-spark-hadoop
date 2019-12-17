from pyspark import SparkContext, SparkConf
import pysnooper
import enchant
import os
from collections import defaultdict
import timeit
import PathList
import pysnooper
import json

def word_count():
    '''count words of palindrome and anagram respectively'''
    # change stop_file, filename, file_update
    stop_file = 142 #current json stops point
    filename = str(stop_file) + "_" + "richey-c.json" #current json file 
    file_update = "dean-c.json"  #need to be added
    filename_update =  str(stop_file + 1) + "_" + file_update
    #main json files
    with open('out/spark-palindrome/' + filename) as f:
        dic_palindrome = json.load(f)
    with open('out/spark-anagram/' + filename) as f:
        dic_anagram = json.load(f)
    
    #json files about ot be updated
    with open('out/' + file_update) as f:
        dic_p = json.load(f)
    with open('out/' + file_update) as f:
        dic_a = json.load(f)

    dic_palindrome_copy = merge_dict(dic_p, dic_palindrome) 
    dic_palindrome.update(dic_palindrome_copy)            
    dic_anagram_copy = merge_dict(dic_a, dic_anagram) 
    dic_anagram.update(dic_anagram_copy)

    #store words into json file
    file_palindrome_path = "out/spark-palindrome/" + filename_update
    with open(file_palindrome_path, 'w') as outfile:
        json.dump(dic_palindrome, outfile)
    file_anagram_path = "out/spark-anagram/" + filename_update
    with open(file_anagram_path, 'w') as outfile:
        json.dump(dic_anagram, outfile)


    print("================================================================")     
    print("Palindrome") 
    print(dic_palindrome) 
    print("=============================")
    print("Anagram") 
    group_dic_anagram = group_anagram(dic_anagram)
    print(group_dic_anagram)
    print("================================================================")
    

def merge_dict(dict1, dict2):
   ''' Merge dictionaries and keep values of common keys in list'''
   dict3 = {**dict1, **dict2}
   for key, value in dict3.items():
       if key in dict1 and key in dict2:
               dict3[key] = int(value) + int (dict1[key])
 
   return dict3

def words_filter(wordCounts):
    '''filter words'''
    d = enchant.Dict("en_US") #english word
    contents_anagram = list_anagram()
    dic_anagram = {}
    dic_palindrome = {}
    for word, count in wordCounts.items():
        if len(word) > 2: #a work must contain more than 2 letters
            if d.check(word): #if it is a english word
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



