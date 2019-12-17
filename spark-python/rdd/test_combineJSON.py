import pysnooper
import os
from collections import defaultdict
import timeit
import PathList
import pysnooper
import json

from os import listdir
from os.path import isfile, join

def word_count():
    '''count words of palindrome and anagram respectively'''
    #json files palindrome
    with open("out/invalid/invalid-palindrome.json") as f:
        dic_palindrome = json.load(f)
    with open("out/invalid/palindrome.json") as f:
        dic_p = json.load(f)
    dic_palindrome_copy = merge_dict(dic_p, dic_palindrome) 
    dic_palindrome.update(dic_palindrome_copy)            
    #anagram
    with open("out/invalid/invalid-anagram.json") as f:
        dic_anagram = json.load(f)   
    with open("out/invalid/anagram.json") as f:
        dic_a = json.load(f)   
    dic_anagram_copy = merge_dict(dic_a, dic_anagram) 
    dic_anagram.update(dic_anagram_copy)

    #store words into json file
    file_palindrome_path = "out/invalid/final-palindrome.json"
    with open(file_palindrome_path, 'w') as outfile:
        json.dump(dic_palindrome, outfile)
    file_anagram_path = "out/invalid/final-anagram.json"
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



