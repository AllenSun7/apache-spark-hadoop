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
    with open("out/invalid/final-palindrome.json") as f:
        dic_palindrome = json.load(f)          
    #anagram
    with open("out/invalid/final-anagram.json") as f:
        dic_anagram = json.load(f)   
    group_dic_anagram = group_anagram(dic_anagram)

    #store words into json file
    f_palindrome = open("out/invalid/final-palindrome.txt", 'w+')
    for item in dic_palindrome.items():
        f_palindrome.write(str(item) + '\n')            
    f_palindrome.close()
    f_angram = open("out/invalid/final-anagram.txt", 'w+')
    for line in group_dic_anagram:
        f_angram.write(str(line) + '\n')
    f_angram.close()


    
    print("================================================================")     
    print("Palindrome") 
    print(dic_palindrome) 
    print("=============================")
    print("Anagram") 
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



