from pyspark import SparkContext, SparkConf
import pysnooper
import enchant
import os
from collections import defaultdict
import timeit
import path_list_all

def word_count():
    '''count words of palindrome and anagram respectively'''
    conf = SparkConf().setAppName("Apache spark").setMaster("local[5]") # 4 cores [*] all available cores
    sc = SparkContext(conf = conf)
    parent_path = "in/maildir/allen-p"
    dic_palindrome = {}
    dic_anagram = {}   
    path_list = get_all_path(parent_path)
    for lines_path in path_list:
        lines = sc.textFile(lines_path) 
        words = lines.flatMap(lambda line: line.split(" "))  
        wordCounts = words.countByValue()
        dic_p, dic_a = words_filter(wordCounts)
        dic_palindrome_copy = merge_dict(dic_p, dic_palindrome) 
        dic_palindrome.update(dic_palindrome_copy)            
        dic_anagram_copy = merge_dict(dic_a, dic_anagram) 
        dic_anagram.update(dic_anagram_copy)

    print("================================================================")    
    print(path_list)
    print("number of path_list: ", len(path_list))
    print("=============================")  
    print("Palindrome") 
    print(dic_palindrome) 
    print("=============================")
    print("Anagram") 
    group_dic_anagram = group_anagram(dic_anagram)
    print(group_dic_anagram)
    print("================================================================")


def get_all_path(parent_path):
    '''return all direstoray paths'''
    names = get_immediate_subdirectories(parent_path)
    path_list = []
    for sub_name in names:
        sub_sub_path, sub_sub_names = get_sub_directory(parent_path, sub_name)
        if sub_sub_names:
            for sub_sub_name in sub_sub_names:
                sub_sub_sub_path, sub_sub_sub_names = get_sub_directory(sub_sub_path, sub_sub_name)
                if sub_sub_sub_names:
                    for sub_sub_sub_name in sub_sub_sub_names:
                        sub_sub_sub_sub_path, sub_sub_sub_sub_names = get_sub_directory(sub_sub_sub_path, sub_sub_sub_name)
                        if sub_sub_sub_sub_names:
                            for sub_sub_sub_sub_name in sub_sub_sub_sub_names:
                                sub_sub_sub_sub_sub_path, sub_sub_sub_sub_sub_names = get_sub_directory(sub_sub_sub_sub_path, sub_sub_sub_sub_name)
                                if sub_sub_sub_sub_sub_names:
                                    for sub_sub_sub_sub_sub_name in sub_sub_sub_sub_sub_names:
                                        sub_sub_sub_sub_sub_sub_path, sub_sub_sub_sub_sub_sub_names = get_sub_directory(sub_sub_sub_sub_path, sub_sub_sub_sub_name)                                        
                                        if sub_sub_sub_sub_sub_sub_names:
                                            for sub_sub_sub_sub_sub_sub_name in sub_sub_sub_sub_sub_sub_names:
                                                path_list.append(sub_sub_sub_sub_sub_sub_path  + "/" + sub_sub_sub_sub_sub_sub_name + "/*")
                                    
                                        else:
                                            path_list.append(sub_sub_sub_sub_sub_path  + "/" + sub_sub_sub_sub_sub_name + "/*")

                                else:    
                                    path_list.append(sub_sub_sub_sub_path  + "/" + sub_sub_sub_sub_name + "/*")
                                
                        else:
                            path_list.append(sub_sub_sub_path + "/" + sub_sub_sub_name + "/*")
                
                else:
                    path_list.append(sub_sub_path + "/" + sub_sub_name + "/*")

        else:
            path_list.append(parent_path + "/" + sub_name + "/*")
    return path_list

def get_sub_directory(path, names):
    sublines_path = path + "/" + names
    return (sublines_path, get_immediate_subdirectories(sublines_path))      

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
    return str(res)

def get_immediate_subdirectories(a_dir):
    '''get subdiretory of dataset'''
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def main():
    '''cauculate runtime'''
    start = timeit.default_timer()
    word_count()
    stop = timeit.default_timer()
    time = stop - start
    print('Runtime: ', time)  

if __name__ == "__main__":
    main()



