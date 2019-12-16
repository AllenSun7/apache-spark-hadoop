from pyspark import SparkContext, SparkConf
import enchant
import timeit
import pysnooper
import os


def word_count():
    #conf = SparkConf().setAppName("word count").setMaster("local[5]")
    #sc = SparkContext(conf = conf)
    parent_path = "in/maildir"
    path_list = get_all_path(parent_path)
    print(path_list)
    print("number of path_list: ", len(path_list))
    

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

def get_words_count(path, name, sc):
    '''run word count'''
    lines_path = path + "/" + name + "/*"
    lines = sc.textFile(lines_path) 
    lines_filter = lines.filter(get_palindrome)
    words = lines_filter.flatMap(lambda line: line.split(" "))
    wordCounts = words.countByValue()
    print(wordCounts)
    return lines_path

def get_sub_directory(path, names):
    sublines_path = path + "/" + names
    return (sublines_path, get_immediate_subdirectories(sublines_path))      

def get_immediate_subdirectories(a_dir):
    '''get subdiretory of dataset'''
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def get_palindrome(word):
    '''palindrome'''
    #not same characters: "AAA","BBB"...
    return (len(word) > 2 and \
            word == word[::-1] and \
            not all(c == word[0] for c in word[1:]))  


def main():
    '''cauculate runtime'''
    path_list = []
    start = timeit.default_timer()
    word_count()
    stop = timeit.default_timer()
    print('Runtime: ', stop - start) 

if __name__ == "__main__":
    main()